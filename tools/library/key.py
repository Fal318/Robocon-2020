"""key.py"""
# -*- coding: utf-8 -*-

KEYNAME = tuple(["C", "CS", "D", "DS", "E", "F",
                 "FS", "G", "GS", "A", "AS", "B"])

CHORD_TO_VALUES = {
    "CO": 0, "COm": 1, "CO7": 2, "COm7": 3, "COdm": 4,
    "CSO": 5, "CSOm": 6, "CSO7": 7, "CSOm7": 8, "CSOdm": 9,
    "DO": 10, "DOm": 11, "DO7": 12, "DOm7": 13, "DOdm": 14,
    "DSO": 15, "DSOm": 16, "DSO7": 17, "DSOm7": 18, "DSOdm": 19,
    "EO": 20, "EOm": 21, "EO7": 22, "EOm7": 23, "EOdm": 24,
    "FO": 25, "FOm": 26, "FO7": 27, "FOm7": 28, "FOdm": 29,
    "FSO": 30, "FSOm": 21, "FSO7": 22, "FSOm7": 33, "FSOdm": 34,
    "GO": 35, "GOm": 36, "GO7": 37, "GOm7": 38, "GOdm": 39,
    "GSO": 40, "GSOm": 41, "GSO7": 42, "GSOm7": 43, "GSOdm": 44,
    "AO": 45, "AOm": 46, "AO7": 47, "AOm7": 48, "AOdm": 49,
    "ASO": 50, "ASOm": 51, "ASO7": 52, "ASOm7": 53, "ASOdm": 54,
    "BO": 55, "BOm": 56, "BO7": 57, "BOm7": 58, "BOdm": 59,

}

KEY_TO_CHORD = {
    # メジャー
    tuple(["C", "E", "G"]): "CO", tuple(["CS", "ES", "GS"]): "CSO",
    tuple(["A", "D", "FS"]): "DO", tuple(["AS", "DS", "F"]): "DSO",
    tuple(["B", "E", "GS"]): "EO", tuple(["A", "C", "F"]): "FO",
    tuple(["AS", "CS", "FS"]): "FSO", tuple(["B", "D", "G"]): "GO",
    tuple(["BS", "DS", "GS"]): "GSO", tuple(["A", "CS", "E"]): "AO",
    tuple(["AS", "CS", "ES"]): "ASO", tuple(["B", "DS", "FS"]): "BO",
    # マイナー
    tuple(["C", "DS", "G"]): "COm", tuple(["CS", "E", "GS"]): "CSOm",
    tuple(["A", "D", "F"]): "DOm", tuple(["AS", "DS", "FS"]): "DSOm",
    tuple(["B", "E", "G"]): "EOm", tuple(["A", "C", "GS"]): "FOm",
    tuple(["A", "CS", "FS"]): "FSOm", tuple(["AS", "D", "G"]): "GOm",
    tuple(["B", "DS", "GS"]): "GSOm", tuple(["A", "C", "E"]): "AOm",
    tuple(["AS", "CS", "ES"]): "ASOm", tuple(["B", "DS", "FS"]): "BOm",
    # セブンス
    tuple(["AS",  "C", "E", "G", ]): "CO7", tuple(["B", "CS", "ES", "GS"]): "CSO7",
    tuple(["A", "C", "D", "FS"]): "DO7", tuple(["AS", "CS", "DS" "G"]): "DSO7",
    tuple(["B", "D", "E", "GS"]): "EO7", tuple(["A", "C", "DS", "F"]): "FO7",
    tuple(["AS", "CS", "E", "FS"]): "FSO7", tuple(["B", "D", "F", "G"]): "GO7",
    tuple(["C", "DS", "FS", "GS"]): "GSO7", tuple(["A", "CS", "E", "G"]): "AO7",
    tuple(["AS", "D", "F", "GS"]): "ASO7", tuple(["A", "B", "DS", "FS"]): "BO7",
    # マイナーセブンス
    tuple(["B", "C", "E", "G"]): "COm7", tuple(["BS", "CS", "ES", "GS"]): "CSOm7",
    tuple(["A", "CS", "D", "FS"]): "DOm7", tuple(["AS", "D", "DS", "G"]): "DSOm7",
    tuple(["B", "DS", "E", "GS"]): "EOm7", tuple(["A", "C", "E", "F"]): "FOm7",
    tuple(["AS", "CS", "F", "FS"]): "FSOm7", tuple(["B", "D", "FS", "G"]): "GOm7",
    tuple(["C", "DS", "G", "GS"]): "GSOm7", tuple(["A", "CS", "E", "GS"]): "AOm7",
    tuple(["A", "AS", "D", "F"]): "ASOm7", tuple(["AS", "B", "DS", "FS"]): "BOm7",  # ここまで
    # ディミニッシュ
    tuple(["C", "DS", "FS"]): "COdm", tuple(["CS", "E", "G"]): "CSOdm",
    tuple(["D", "F", "GS"]): "DOdm", tuple(["A", "FS", "DS"]): "DSOdm",
    tuple(["AS", "G", "E"]): "EOdm", tuple(["B", "GS", "F"]): "FOdm",
    tuple(["AS", "CS", "G"]): "FSOdm", tuple(["CS", "G", "GS"]): "GOdm",
    tuple(["B", "D", "GS"]): "GSOdm", tuple(["A", "C", "DS"]): "AOdm",
    tuple(["AS", "CS", "E"]): "ASOdm", tuple(["B", "D", "F"]): "BOdm",
}


def key_to_value(*args):
    chord = KEY_TO_CHORD[args]
    return CHORD_TO_VALUES[chord]


if __name__ == "__main__":
    pass
