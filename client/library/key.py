"""key.py"""
# -*- coding: utf-8 -*-

KEYNAME = tuple(["C", "C#", "D", "D#", "E", "F",
                 "F#", "G", "G#", "A", "A#", "B"])

KEY = {
    "C": 4, "Cm": 16, "C7": 28, "Cm7": 40, "Cdm": 52,
    "C#": 5, "C#m": 17, "C#7": 29, "C#m7": 41, "C#dm": 53,
    "D": 6, "Dm": 18, "D7": 30, "Dm7": 42, "Ddm": 54,
    "D#": 7, "D#m": 19, "D#7": 31, "D#m7": 43, "D#dm": 55,
    "E": 8, "Em": 20, "E7": 32, "Em7": 44, "Edm": 56,
    "F": 9, "Fm": 21, "F7": 33, "Fm7": 45, "Fdm": 57,
    "F#": 10, "F#m": 22, "F#7": 34, "F#m7": 46, "F#dm": 58,
    "G": 11, "Gm": 23, "G7": 35, "Gm7": 47, "Gdm": 59,
    "G#": 12, "G#m": 24, "G#7": 36, "G#m7": 48, "G#dm": 60,
    "A": 13, "Am": 25, "A7": 37, "Am7": 49, "Adm": 61,
    "A#": 14, "A#m": 26, "A#7": 38, "A#m7": 50, "A#dm": 62,
    "B": 15, "Bm": 27, "B7": 39, "Bm7": 51, "Bdm": 63,

}

CHORD = {
    # 単音
    tuple(["C"]): "C", tuple(["C#"]): "C#", tuple(["D"]): "D", tuple(["D#"]): "D#",
    tuple(["E"]): "E", tuple(["F"]): "F", tuple(["F#"]): "F#", tuple(["G"]): "G",
    tuple(["G#"]): "G#", tuple(["A"]): "A", tuple(["A#"]): "A#", tuple(["B"]): "B",

    # メジャー
    tuple(["C", "E", "G"]): "CM", tuple(["C#", "F", "G#"]): "C#M",
    tuple(["A", "D", "F#"]): "DM", tuple(["A#", "D#", "G"]): "D#M",
    tuple(["B", "E", "G#"]): "EM", tuple(["A", "C", "F"]): "FM",
    tuple(["A#", "C#", "F#"]): "F#M", tuple(["B", "D", "G"]): "GM",
    tuple(["C", "D#", "G#"]): "G#M", tuple(["A", "C#", "E"]): "AM",
    tuple(["A#", "D", "F"]): "A#M", tuple(["B", "D#", "F#"]): "BM",

    # マイナー
    tuple(["C", "D#", "G"]): "Cm", tuple(["C#", "E", "G#"]): "C#m",
    tuple(["A", "D", "F"]): "Dm", tuple(["A#", "D#", "F#"]): "D#m",
    tuple(["B", "E", "G"]): "Em", tuple(["C", "F", "G#"]): "Fm",
    tuple(["A", "C#", "F#"]): "F#m", tuple(["A#", "D", "G"]): "Gm",
    tuple(["B", "D#", "G#"]): "G#m", tuple(["A", "C", "E"]): "Am",
    tuple(["A#", "C#", "F"]): "A#m", tuple(["B", "D", "F#"]): "Bm",

    # セブンス
    tuple(["A#", "C", "E", "G", ]): "C7", tuple(["B", "C#", "F", "G#"]): "C#7",
    tuple(["A", "C", "D", "F#"]): "D7", tuple(["A#", "C#", "D#" "G"]): "D#7",
    tuple(["B", "D", "E", "G#"]): "E7", tuple(["A", "C", "D#", "F"]): "F7",
    tuple(["A#", "C#", "E", "F#"]): "F#7", tuple(["B", "D", "F", "G"]): "G7",
    tuple(["C", "D#", "F#", "G#"]): "G#7", tuple(["A", "C#", "E", "G"]): "A7",
    tuple(["A#", "D", "F", "G#"]): "A#7", tuple(["A", "B", "D#", "F#"]): "B7",

    # マイナーセブンス
    tuple(["A#", "C", "D#", "G"]): "Cm7", tuple(["B", "C#", "E", "G#"]): "C#m7",
    tuple(["A", "C", "D", "F"]): "Dm7", tuple(["A#", "C#", "D#", "F#"]): "D#m7",
    tuple(["B", "D", "E", "G"]): "Em7", tuple(["C", "D#", "F", "G#"]): "Fm7",
    tuple(["A", "C#", "E", "F#"]): "F#m7", tuple(["A#", "D", "F", "G"]): "Gm7",
    tuple(["B", "D#", "F#", "G#"]): "G#m7", tuple(["A", "C", "E", "G"]): "Am7",
    tuple(["A#", "C#", "F", "G#"]): "A#m7", tuple(["A", "B", "D", "F#"]): "Bm7",

    # ディミニッシュ
    tuple(["C", "D#", "F#"]): "Cdm", tuple(["C#", "E", "G"]): "C#dm",
    tuple(["D", "F", "G#"]): "Ddm", tuple(["A", "F#", "D#"]): "D#dm",
    tuple(["A#", "G", "E"]): "Edm", tuple(["B", "G#", "F"]): "Fdm",
    tuple(["A", "C", "F#"]): "F#dm", tuple(["A#", "C#", "G"]): "Gdm",
    tuple(["B", "D", "G#"]): "G#dm", tuple(["A", "C", "D#"]): "Adm",
    tuple(["A#", "C#", "E"]): "A#dm", tuple(["B", "D", "F"]): "Bdm",
}

PITCH = {
    0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F", 6: "F#", 7: "G",
    8: "G#", 9: "A", 10: "A#", 11: "B", 12: "C", 13: "C#", 14: "D",
    15: "D#", 16: "E", 17: "F", 18: "F#", 19: "G", 20: "G#", 21: "A",
    22: "A#", 23: "B", 24: "C", 25: "C#", 26: "D", 27: "D#", 28: "E",
    29: "F", 30: "F#", 31: "G", 32: "G#", 33: "A", 34: "A#", 35: "B",
    36: "C", 37: "C#", 38: "D", 39: "D#", 40: "E", 41: "F", 42: "F#",
    43: "G", 44: "G#", 45: "A", 46: "A#", 47: "B", 48: "C", 49: "C#",
    50: "D", 51: "D#", 52: "E", 53: "F", 54: "F#", 55: "G", 56: "G#",
    57: "A", 58: "A#", 59: "B", 60: "C", 61: "C#", 62: "D", 63: "D#",
    64: "E", 65: "F", 66: "F#", 67: "G", 68: "G#", 69: "A", 70: "A#",
    71: "B", 72: "C", 73: "C#", 74: "D", 75: "D#", 76: "E", 77: "F",
    78: "F#", 79: "G", 80: "G#", 81: "A", 82: "A#", 83: "B", 84: "C",
    85: "C#", 86: "D", 87: "D#", 88: "E", 89: "F", 90: "F#", 91: "G",
    92: "G#", 93: "A", 94: "A#", 95: "B", 96: "C", 97: "C#", 98: "D",
    99: "D#", 100: "E", 101: "F", 102: "F#", 103: "G", 104: "G#",
    105: "A", 106: "A#", 107: "B", 108: "C", 109: "C#", 110: "D",
    111: "D#", 112: "E", 113: "F", 114: "F#", 115: "G", 116: "G#",
    117: "A", 118: "A#", 119: "B", 120: "C", 121: "C#", 122: "D",
    123: "D#", 124: "E", 125: "F", 126: "F#", 127: "G",

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
