import numpy as np
from numpy.lib.ufunclike import fix
import pandas as pd
from library import key

DEFAULT_HEADER = ["bar", "sbar", "note",
                  "chord", "castanets", "shaker", "tambourine"]
HEADER = ["BPM", "TIMING", "STRING", "FRET1", "FRET2", "FRET3", "FRET4", "STROKE",
          "CHORD", "FACE", "NECK", "CASTANETS", "SHAKER", "TAMBOURINE", "MOTION", "COLOR"]

SINGLE_SOUND = {
    "nan": [[0, 0]],
    "D": [[2, 3]],
    "DS": [[3, 3]],
    "E": [[4, 3]],
    "F": [[1, 2], [5, 3]],
    "FS": [[2, 2], [6, 3]],
    "G": [[3, 2], [7, 3]],
    "GS": [[1, 4],  [4, 2], [8, 3]],
    "A": [[2, 4], [5, 2]],
    "AS": [[3, 4], [6, 2], [1, 1]],
    "B": [[4, 4], [7, 2], [2, 1]],
    "C2": [[5, 4], [8, 2], [3, 1]],
    "CS2": [[6, 4], [4, 1]],
    "D2": [[7, 4], [5, 1]],
    "D2S": [[8, 4], [6, 1]],
    "E2": [[7, 1]],
    "F2": [[8, 1]],
}


def search(note: list) -> list:
    status = BowStatus()
    return [status.decide_bowstrings(n, i) for i, n in enumerate(note)]


class BowStatus:
    def __init__(self):
        self.__bowstrings = [0 for i in range(4)]

    def decide_bowstrings(self, note: str, loopcount: int) -> list:
        """
        loopcount:16*小節+分小節
        """
        if note == "nan":
            return [0, 0]
        can_use_bow = np.argsort(self.__bowstrings)  # 最後に使われてからの時間が長い弦
        candidacy_bow = SINGLE_SOUND[note]  # その音を鳴らすことができる弦
        for can_use in can_use_bow:
            for bow in candidacy_bow:
                if can_use == bow[1]-1:
                    self.__bowstrings[can_use] = loopcount
                    return bow  # フレット , 弦


def get_songs_length(df: pd.DataFrame) -> int:
    return (max(df["BAR"])+1)*16


def generate_fixed_chord(df: pd.DataFrame, fixed_list: list) -> list:
    for bar, sbar, chord in zip(df["BAR"], df["SBAR"], df["CHORD"]):
        index = bar*16+sbar
        fixed_list[index] = key.CHORD_TO_VALUES[chord]
    return fixed_list


def fix_df(df, length: int):
    arr = ["nan" for _ in range(length)]
    for _, row in df.iterrows():
        if not isinstance(row["NOTE"], float):
            arr[row["BAR"]*16+row["SBAR"]-17] = row["NOTE"]
    return arr


def main():

    BPM = int(input("BPMを入力してください"))
    df = pd.read_csv("../data/original/365.csv")
    print(np.unique(df["NOTE"].dropna()))
    fixed_df = pd.DataFrame(
        [[np.NaN for _ in range(len(HEADER))] for _ in range(get_songs_length(df))], columns=HEADER)
    fixed_df["CHORD"] = generate_fixed_chord(df, fixed_df["CHORD"])
    fixed_df["BPM"] = fixed_df["BPM"].fillna(BPM)
    fret = [fixed_df["FRET1"].fillna(0)for _ in range(4)]
    searched = search(fix_df(df, get_songs_length(df))[::-1])[::-1]
    fixed_df["STROKE"] = [1 if s[1] else 0 for s in searched]
    for index, row in enumerate(searched):
        if row is not [0, 0]:
            fret[row[1]-1][index] = row[0]
    for i, f in enumerate(fret):
        lastdata = 0
        fix_fret = []
        for row in f[::-1]:
            if row == 0:
                fix_fret.append(lastdata)
            else:
                lastdata = row
                fix_fret.append(row)
        fixed_df[f"FRET{i+1}"] = fix_fret[::-1]

    fixed_df["STRING"] = [np.nan if s[1] == 0 else s[1]for s in searched]
    fixed_df["STRING"] = fixed_df["STRING"].fillna(method='bfill').fillna(0)
    fixed_chord = [np.nan for _ in range(get_songs_length(df))]
    for bar, sbar, chord in zip(df["BAR"], df["SBAR"], df["CHORD"]):
        fixed_chord[bar*16+sbar-17] = chord
    fixed_df["CHORD"] = [key.CHORD_TO_VALUES[d] for d in fixed_chord]
    fixed_df["TIMING"] = [
        1 if (i//2) % 2 == 0 else 0 for i in range(len(fixed_df["TIMING"]))]
    for head in ["MOTION", "COLOR", "FACE", "NECK"]:
        fixed_df[head] = fixed_df[head].fillna(0)
    for head in ["CASTANETS", "SHAKER", "TAMBOURINE"]:
        fixed_df[head] = df[head].fillna(0)
    for header in HEADER:
        try:
            fixed_df[header] = fixed_df[header].astype(int)
        except:
            pass
    fixed_df.to_csv("../data/fixed/365.csv", index=False)


if __name__ == "__main__":
    main()
