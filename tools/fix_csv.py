import sys
import threading
import numpy as np
from numpy.lib.ufunclike import fix
import pandas as pd
from library import key

sys.setrecursionlimit(10000000)

HEADER = ["BPM", "TIMING", "STRING", "FRET1", "FRET2", "FRET3", "FRET4", "STROKE",
          "CHORD", "FACE", "NECK", "CASTANETS", "SHAKER", "TAMBOURINE", "MOTION", "COLOR"]
"""
SINGLE_SOUND = {
    "CS": [[1, 3]],
    "D": [[2, 3]],
    "DS": [[3, 3]],
    "E": [[3, 4]],
    "F": [[5, 3], [1, 2]],
    "FS": [[6, 3], [2, 2]],
    "G": [[7, 3], [3, 2]],
    "GS": [[1, 4], [8, 3], [4, 2]],
    "A": [[2, 4], [5, 2]],
    "AS": [[3, 4], [6, 2], [1, 1]],
    "B": [[4, 4], [7, 2], [2, 1]],
    "C2": [[5, 4], [8, 2], [3, 1]],
    "C2S": [[6, 4], [4, 1]],
    "D2": [[7, 4], [5, 1]],
    "D2S": [[8, 4], [6, 1]],
    "E2": [[7, 1]],
    "F2": [[8, 1]],
}
"""
SINGLE_SOUND = {
    "nan": [[0, 0]],
    "D": [[2, 3]],
    "DS": [[3, 3]],
    "E": [[3, 4]],
    "F": [[5, 3], [1, 2]],
    "FS": [[6, 3], [2, 2]],
    "G": [[7, 3], [3, 2]],
    "GS": [[1, 4], [8, 3], [4, 2]],
    "A": [[2, 4], [5, 2]],
    "AS": [[3, 4], [6, 2], [1, 1]],
    "B": [[4, 4], [7, 2], [2, 1]],
    "C": [[5, 4], [8, 2], [3, 1]],
    "CS": [[6, 4], [4, 1]],
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
    return (max(df["bar"])+1)*16


def generate_fixed_chord(df: pd.DataFrame, fixed_list: list) -> list:
    for bar, sbar, chord in zip(df["bar"], df["sbar"], df["chord"]):
        index = bar*16+sbar
        fixed_list[index] = key.CHORD_TO_VALUES[chord]
    return fixed_list


def fix_df(df, length: int):
    arr = ["nan" for _ in range(length)]
    for _, row in df.iterrows():
        if not isinstance(row["note"], float):
            arr[row["bar"]*16+row["sbar"]-17] = row["note"]
    return arr


def main():
    BPM = int(input("BPMを入力してください"))
    df = pd.read_csv("../data/original/365.csv")
    fixed_df = pd.DataFrame(
        [[np.NaN for _ in range(len(HEADER))] for _ in range(get_songs_length(df))], columns=HEADER)
    fixed_df["CHORD"] = generate_fixed_chord(df, fixed_df["CHORD"])
    fixed_df["BPM"] = fixed_df["BPM"].fillna(BPM)
    fixed_df["note"] = search(fix_df(df, get_songs_length(df)))
    """
    for header in HEADER:
        fixed_df[header] = fixed_df[header].astype(int)
    """
    fixed_df.to_csv("../data/fixed/365.csv")


if __name__ == "__main__":
    main()
