"""key.py"""
# -*- coding: utf-8 -*-

KEYNAME = tuple(["C", "CS", "D", "DS", "E", "F",
                 "FS", "G", "GS", "A", "AS", "B"])

KEY = {
    "C": 4, "Cm": 16, "C7": 28, "Cm7": 40, "Cdm": 52,
    "CS": 5, "CSm": 17, "CS7": 29, "CSm7": 41, "CSdm": 53,
    "D": 6, "Dm": 18, "D7": 30, "Dm7": 42, "Ddm": 54,
    "DS": 7, "DSm": 19, "DS7": 31, "DSm7": 43, "DSdm": 55,
    "E": 8, "Em": 20, "E7": 32, "Em7": 44, "Edm": 56,
    "F": 9, "Fm": 21, "F7": 33, "Fm7": 45, "Fdm": 57,
    "FS": 10, "FSm": 22, "FS7": 34, "FSm7": 46, "FSdm": 58,
    "G": 11, "Gm": 23, "G7": 35, "Gm7": 47, "Gdm": 59,
    "GS": 12, "GSm": 24, "GS7": 36, "GSm7": 48, "GSdm": 60,
    "A": 13, "Am": 25, "A7": 37, "Am7": 49, "Adm": 61,
    "AS": 14, "ASm": 26, "AS7": 38, "ASm7": 50, "ASdm": 62,
    "B": 15, "Bm": 27, "B7": 39, "Bm7": 51, "Bdm": 63,

}

CHORD = {
    # 単音
    tuple(["C"]): "C", tuple(["CS"]): "CS", tuple(["D"]): "D", tuple(["DS"]): "DS",
    tuple(["E"]): "E", tuple(["F"]): "F", tuple(["FS"]): "FS", tuple(["G"]): "G",
    tuple(["GS"]): "GS", tuple(["A"]): "A", tuple(["AS"]): "AS", tuple(["B"]): "B",

    # メジャー
    tuple(["C", "E", "G"]): "CM", tuple(["CS", "F", "GS"]): "CSM",
    tuple(["A", "D", "FS"]): "DM", tuple(["AS", "DS", "G"]): "DSM",
    tuple(["B", "E", "GS"]): "EM", tuple(["A", "C", "F"]): "FM",
    tuple(["AS", "CS", "FS"]): "FSM", tuple(["B", "D", "G"]): "GM",
    tuple(["C", "DS", "GS"]): "GSM", tuple(["A", "CS", "E"]): "AM",
    tuple(["AS", "D", "F"]): "ASM", tuple(["B", "DS", "FS"]): "BM",

    # マイナー
    tuple(["C", "DS", "G"]): "Cm", tuple(["CS", "E", "GS"]): "CSm",
    tuple(["A", "D", "F"]): "Dm", tuple(["AS", "DS", "FS"]): "DSm",
    tuple(["B", "E", "G"]): "Em", tuple(["C", "F", "GS"]): "Fm",
    tuple(["A", "CS", "FS"]): "FSm", tuple(["AS", "D", "G"]): "Gm",
    tuple(["B", "DS", "GS"]): "GSm", tuple(["A", "C", "E"]): "Am",
    tuple(["AS", "CS", "F"]): "ASm", tuple(["B", "D", "FS"]): "Bm",

    # セブンス
    tuple(["AS", "C", "E", "G", ]): "C7", tuple(["B", "CS", "F", "GS"]): "CS7",
    tuple(["A", "C", "D", "FS"]): "D7", tuple(["AS", "CS", "DS" "G"]): "DS7",
    tuple(["B", "D", "E", "GS"]): "E7", tuple(["A", "C", "DS", "F"]): "F7",
    tuple(["AS", "CS", "E", "FS"]): "FS7", tuple(["B", "D", "F", "G"]): "G7",
    tuple(["C", "DS", "FS", "GS"]): "GS7", tuple(["A", "CS", "E", "G"]): "A7",
    tuple(["AS", "D", "F", "GS"]): "AS7", tuple(["A", "B", "DS", "FS"]): "B7",

    # マイナーセブンス
    tuple(["AS", "C", "DS", "G"]): "Cm7", tuple(["B", "CS", "E", "GS"]): "CSm7",
    tuple(["A", "C", "D", "F"]): "Dm7", tuple(["AS", "CS", "DS", "FS"]): "DSm7",
    tuple(["B", "D", "E", "G"]): "Em7", tuple(["C", "DS", "F", "GS"]): "Fm7",
    tuple(["A", "CS", "E", "FS"]): "FSm7", tuple(["AS", "D", "F", "G"]): "Gm7",
    tuple(["B", "DS", "FS", "GS"]): "GSm7", tuple(["A", "C", "E", "G"]): "Am7",
    tuple(["AS", "CS", "F", "GS"]): "ASm7", tuple(["A", "B", "D", "FS"]): "Bm7",

    # ディミニッシュ
    tuple(["C", "DS", "FS"]): "Cdm", tuple(["CS", "E", "G"]): "CSdm",
    tuple(["D", "F", "GS"]): "Ddm", tuple(["A", "FS", "DS"]): "DSdm",
    tuple(["AS", "G", "E"]): "Edm", tuple(["B", "GS", "F"]): "Fdm",
    tuple(["A", "C", "FS"]): "FSdm", tuple(["AS", "CS", "G"]): "Gdm",
    tuple(["B", "D", "GS"]): "GSdm", tuple(["A", "C", "DS"]): "Adm",
    tuple(["AS", "CS", "E"]): "ASdm", tuple(["B", "D", "F"]): "Bdm",
}

PITCH = {
    0: "C", 1: "CS", 2: "D", 3: "DS", 4: "E", 5: "F", 6: "FS", 7: "G",
    8: "GS", 9: "A", 10: "AS", 11: "B", 12: "C", 13: "CS", 14: "D",
    15: "DS", 16: "E", 17: "F", 18: "FS", 19: "G", 20: "GS", 21: "A",
    22: "AS", 23: "B", 24: "C", 25: "CS", 26: "D", 27: "DS", 28: "E",
    29: "F", 30: "FS", 31: "G", 32: "GS", 33: "A", 34: "AS", 35: "B",
    36: "C", 37: "CS", 38: "D", 39: "DS", 40: "E", 41: "F", 42: "FS",
    43: "G", 44: "GS", 45: "A", 46: "AS", 47: "B", 48: "C", 49: "CS",
    50: "D", 51: "DS", 52: "E", 53: "F", 54: "FS", 55: "G", 56: "GS",
    57: "A", 58: "AS", 59: "B", 60: "C", 61: "CS", 62: "D", 63: "DS",
    64: "E", 65: "F", 66: "FS", 67: "G", 68: "GS", 69: "A", 70: "AS",
    71: "B", 72: "C", 73: "CS", 74: "D", 75: "DS", 76: "E", 77: "F",
    78: "FS", 79: "G", 80: "GS", 81: "A", 82: "AS", 83: "B", 84: "C",
    85: "CS", 86: "D", 87: "DS", 88: "E", 89: "F", 90: "FS", 91: "G",
    92: "GS", 93: "A", 94: "AS", 95: "B", 96: "C", 97: "CS", 98: "D",
    99: "DS", 100: "E", 101: "F", 102: "FS", 103: "G", 104: "GS",
    105: "A", 106: "AS", 107: "B", 108: "C", 109: "CS", 110: "D",
    111: "DS", 112: "E", 113: "F", 114: "FS", 115: "G", 116: "GS",
    117: "A", 118: "AS", 119: "B", 120: "C", 121: "CS", 122: "D",
    123: "DS", 124: "E", 125: "F", 126: "FS", 127: "G",

}


def pitch_to_key(pitch: int) -> str:
    return PITCH[pitch]


def key_to_chord(key: list = None):
    try:
        return CHORD[key]
    except KeyError:
        return key


def pitch_to_chord(pitches: list = None):
    key = []
    for pitch in pitches:
        key.append(pitch_to_key(pitch))
    key = list(set(key))
    key.sort()
    return key_to_chord(tuple(key))


def chord_to_value(key: list = None, stroke: bool = False) -> int:
    chord = key_to_chord(key)
    if chord == 0:
        return 1
    if stroke:
        return chord + 3
    return chord + 1


if __name__ == "__main__":
    pass
