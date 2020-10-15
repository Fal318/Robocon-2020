"""key.py"""
# -*- coding: utf-8 -*-
import numpy as np
KEYNAME = tuple(["C", "CS", "D", "DS", "E", "F",
                 "FS", "G", "GS", "A", "AS", "B"])

CHORD_TO_VALUES = {
    np.NaN: 0, "nan": 0,
    "C": 1, "Cm": 2, "C7": 3, "Cm7": 4, "Cdm": 5,
    "CS": 6, "CSm": 7, "CS7": 8, "CSm7": 9, "CSdm": 10,
    "D": 11, "Dm": 12, "D7": 13, "Dm7": 14, "Ddm": 15,
    "DS": 16, "DSm": 17, "DS7": 18, "DSm7": 19, "DSdm": 20,
    "E": 21, "Em": 22, "E7": 23, "Em7": 24, "Edm": 25,
    "F": 26, "Fm": 27, "F7": 28, "Fm7": 29, "Fdm": 30,
    "FS": 31, "FSm": 22, "FS7": 23, "FSm7": 34, "FSdm": 35,
    "G": 36, "Gm": 37, "G7": 38, "Gm7": 39, "Gdm": 40,
    "GS": 41, "GSm": 42, "GS7": 43, "GSm7": 44, "GSdm": 45,
    "A": 46, "Am": 47, "A7": 48, "Am7": 49, "Adm": 50,
    "AS": 51, "ASm": 52, "AS7": 53, "ASm7": 54, "ASdm": 55,
    "B": 56, "Bm": 57, "B7": 58, "Bm7": 59, "Bdm": 60,

}

KEY_TO_CHORD = {
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

# フレット , 弦


def key_to_value(*args):
    chrd = KEY_TO_CHORD[args]
    return CHORD_TO_VALUES[chrd]


if __name__ == "__main__":
    pass
