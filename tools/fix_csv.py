import pandas as pd

ROW_SIZE = 7
HEADTYPE = [int, int, str, str, int, int, int]


def data_type(df: pd.DataFrame) -> bool:
    for i, t in enumerate(HEADTYPE):
        if isinstance(df.iloc[i].dtype.type, t):
            pass


def get_songs_length(df: pd.DataFrame) -> int:
    return max(df.iloc[0])


def main():
    pass

    df = pd.read_csv("../data/csv/data.csv")
    fixed_df = pd.DataFrame()
    line_name = [["小節", ""]]
    for old_line, new_line in line_name:
        fixed_df[new_line] = df[old_line]
    for row in df[""]:
        pass
