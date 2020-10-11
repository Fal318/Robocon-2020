"""key.py"""
# -*- cding: utf-8 -*-

KEYNAME = tuple(["C", "CS", "D", "DS", "E", "F",
                 "FS", "G", "GS", "A", "AS", "B"])

CHRD_T_VALUES = {
    "C": 0, "Cm": 1, "C7": 2, "Cm7": 3, "Cdm": 4,
    "CS": 5, "CSm": 6, "CS7": 7, "CSm7": 8, "CSdm": 9,
    "D": 10, "Dm": 11, "D7": 12, "Dm7": 13, "Ddm": 14,
    "DS": 15, "DSm": 16, "DS7": 17, "DSm7": 18, "DSdm": 19,
    "E": 20, "Em": 21, "E7": 22, "Em7": 23, "Edm": 24,
    "F": 25, "Fm": 26, "F7": 27, "Fm7": 28, "Fdm": 29,
    "FS": 30, "FSm": 21, "FS7": 22, "FSm7": 33, "FSdm": 34,
    "G": 35, "Gm": 36, "G7": 37, "Gm7": 38, "Gdm": 39,
    "GS": 40, "GSm": 41, "GS7": 42, "GSm7": 43, "GSdm": 44,
    "A": 45, "Am": 46, "A7": 47, "Am7": 48, "Adm": 49,
    "AS": 50, "ASm": 51, "AS7": 52, "ASm7": 53, "ASdm": 54,
    "B": 55, "Bm": 56, "B7": 57, "Bm7": 58, "Bdm": 59,

}

KEY_T_CHRD = {
    # メジャー
    tuple(["C", "E", "G"]): "C", tuple(["CS", "ES", "GS"]): "CS",
    tuple(["A", "D", "FS"]): "D", tuple(["AS", "DS", "G"]): "DS",
    tuple(["B", "E", "GS"]): "E", tuple(["A", "C", "F"]): "F",
    tuple(["AS", "CS", "FS"]): "FS", tuple(["B", "D", "G"]): "G",
    tuple(["BS", "DS", "GS"]): "GS", tuple(["A", "CS", "E"]): "A",
    tuple(["AS", "D", "F"]): "AS", tuple(["B", "DS", "FS"]): "B",
    # マイナー
    tuple(["C", "DS", "G"]): "Cm", tuple(["CS", "E", "GS"]): "CSm",
    tuple(["A", "D", "F"]): "Dm", tuple(["AS", "DS", "FS"]): "DSm",
    tuple(["B", "E", "G"]): "Em", tuple(["F", "GS", "C"]): "Fm",
    tuple(["A", "CS", "FS"]): "FSm", tuple(["AS", "D", "G"]): "Gm",
    tuple(["B", "DS", "GS"]): "GSm", tuple(["A", "C", "E"]): "Am",
    tuple(["AS", "CS", "ES"]): "ASm", tuple(["B", "D", "FS"]): "Bm",
    # セブンス
    tuple(["AS",  "C", "E", "G", ]): "C7", tuple(["B", "CS", "ES", "GS"]): "CS7",
    tuple(["A", "C", "D", "FS"]): "D7", tuple(["AS", "CS", "DS" "G"]): "DS7",
    tuple(["B", "D", "E", "GS"]): "E7", tuple(["A", "C", "DS", "F"]): "F7",
    tuple(["AS", "CS", "E", "FS"]): "FS7", tuple(["B", "D", "F", "G"]): "G7",
    tuple(["C", "DS", "FS", "GS"]): "GS7", tuple(["A", "CS", "E", "G"]): "A7",
    tuple(["AS", "D", "F", "GS"]): "AS7", tuple(["A", "B", "DS", "FS"]): "B7",
    # マイナーセブンス
    tuple(["B", "C", "E", "G"]): "Cm7", tuple(["CS", "F", "GS", "C"]): "CSm7",
    tuple(["A", "CS", "D", "FS"]): "Dm7", tuple(["AS", "D", "DS", "G"]): "DSm7",
    tuple(["B", "DS", "E", "GS"]): "Em7", tuple(["A", "C", "E", "F"]): "Fm7",
    tuple(["AS", "CS", "F", "FS"]): "FSm7", tuple(["B", "D", "FS", "G"]): "Gm7",
    tuple(["C", "DS", "G", "GS"]): "GSm7", tuple(["A", "CS", "E", "GS"]): "Am7",
    tuple(["A", "AS", "D", "F"]): "ASm7", tuple(["AS", "B", "DS", "FS"]): "Bm7",  # ここまで
    # ディミニッシュ
    tuple(["C", "DS", "FS"]): "Cdm", tuple(["CS", "E", "G"]): "CSdm",
    tuple(["D", "F", "GS"]): "Ddm", tuple(["A", "FS", "DS"]): "DSdm",
    tuple(["AS", "G", "E"]): "Edm", tuple(["B", "GS", "F"]): "Fdm",
    tuple(["A", "C", "FS"]): "FSdm", tuple(["CS", "G", "AS"]): "Gdm",
    tuple(["B", "D", "GS"]): "GSdm", tuple(["A", "C", "DS"]): "Adm",
    tuple(["AS", "CS", "E"]): "ASdm", tuple(["B", "D", "F"]): "Bdm",
}


def key_t_value(*args):
    chrd = KEY_T_CHRD[args]
    return CHRD_T_VALUES[chrd]


if __name__ == "__main__":
    pass
