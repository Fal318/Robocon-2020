# -*- coding: utf-8 -*-
"""楽器ごとに分かれたCSVを一つにまとめる"""
import pandas as pd


def main():
    """main"""
    df_arrys, header = [], []
    for i in range(129):
        try:
            data_frame = pd.read_csv(f"../../data/csv/data_{i}.csv")
        except FileNotFoundError:
            continue
        else:
            header.append(str(i))
            df_arrys.append(data_frame)
    merged__df = pd.DataFrame()
    for data in df_arrys:
        merged__df = pd.concat([merged__df, data], axis=1)

    merged__df.columns = header
    merged__df.to_csv("../../data/csv/merged.csv", index=False)


if __name__ == "__main__":
    main()
