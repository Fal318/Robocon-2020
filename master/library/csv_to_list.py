import pandas as pd
import key
import program_number


def csv_to_senddata(id_num: int) -> list:
    """CSVから送信用データに変換する"""

    program_nums: list = None
    csv_data = pd.read_csv("../data/csv/merged.csv", header=0)

    if id_num == 0:
        program_nums = program_number.UKULELE
    if id_num == 1:
        program_nums = program_number.PERCUSSION
    if program_nums is None:
        return None
    arrs = [[] for _ in range(len(program_nums))]

    for (i, program_num) in enumerate(program_nums):
        for sound in csv_data[str(program_num)]:
            arrs[i].append(str(sound))
    if id_num == 0:
        return [[key.chord_to_value(a) if a != "nan" else 1 for a in arr]for arr in arrs]
    if id_num == 1:
        ret_arr = [[1 for _ in range(len(arrs[0]))]]
        for (i, arr) in enumerate(arrs):
            for (j, element) in enumerate(arr):
                if element != "nan":
                    ret_arr[0][j] += 2**i
        return ret_arr
    return None


if __name__ == "__main__":
    pass
