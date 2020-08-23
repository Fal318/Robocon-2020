# -*- coding: utf-8 -*-
"""key.py"""

KEYNAME = tuple(["C", "C#", "D", "D#", "E", "F",
                 "F#", "G", "G#", "A", "A#", "B"])

KEY = {
    "CM": 4, "Cm": 16, "C7": 28, "Cm7": 40, "Cdm": 52,
    "C#M": 5, "C#m": 17, "C#7": 29, "C#m7": 41, "C#dm": 53,
    "DM": 6, "Dm": 18, "D7": 30, "Dm7": 42, "Ddm": 54,
    "D#M": 7, "D#m": 19, "D#7": 31, "D#m7": 43, "D#dm": 55,
    "EM": 8, "Em": 20, "E7": 32, "Em7": 44, "Edm": 56,
    "FM": 9, "Fm": 21, "F7": 33, "Fm7": 45, "Fdm": 57,
    "F#M": 10, "F#m": 22, "F#7": 34, "F#m7": 46, "F#dm": 58,
    "GM": 11, "Gm": 23, "G7": 35, "Gm7": 47, "Gdm": 59,
    "G#M": 12, "G#m": 24, "G#7": 36, "G#m7": 48, "G#dm": 60,
    "AM": 13, "Am": 25, "A7": 37, "Am7": 49, "Adm": 61,
    "A#M": 14, "A#m": 26, "A#7": 38, "A#m7": 50, "A#dm": 62,
    "BM": 15, "Bm": 27, "B7": 39, "Bm7": 51, "Bdm": 63,
    "C": 64, "C#": 65, "D": 66, "D#": 67, "E": 68, "F": 69,
    "F#": 70, "G": 71, "G#": 72, "A": 73, "A#": 74, "B": 75
}

CHORD = {
    # 単音
    "C": "C", "C#": "C#", "D": "D", "D#": "D#",
    "E": "E", "F": "F", "F#": "F#", "G": "G",
    "G#": "G#", "A": "A", "A#": "A#", "B": "B",

    # メジャー
    "CEG": "CM", "C#FG#": "C#M", "ADF#": "DM",
    "A#D#G": "D#M", "BEG#": "EM", "ACF": "FM",
    "A#C#F#": "F#M", "BDG": "GM", "CD#G#": "G#M",
    "AC#E": "AM", "A#DF": "A#M", "BD#F#": "BM",

    # マイナー
    "CD#G": "Cm", "C#EG#": "C#m", "ADF": "Dm",
    "A#D#F#": "D#m", "BEG": "Em", "CFG#": "Fm",
    "AC#F#": "F#m", "A#DG": "Gm", "BD#G#": "G#m",
    "ACE": "Am", "A#C#F": "A#m", "BDF#": "Bm",

    # セブンス
    "A#CEG": "C7", "BC#FG#": "C#7", "ACDF#": "D7",
    "A#C#D#" "G": "D#7", "BDEG#": "E7", "ACD#F": "F7",
    "A#C#EF#": "F#7", "BDFG": "G7", "CD#F#G#": "G#7",
    "AC#EG": "A7", "A#DFG#": "A#7", "ABD#F#": "B7",

    # マイナーセブンス
    "A#CD#G": "Cm7", "BC#EG#": "C#m7", "ACDF": "Dm7",
    "A#C#D#F#": "D#m7", "BDEG": "Em7", "CD#FG#": "Fm7",
    "AC#EF#": "F#m7", "A#DFG": "Gm7", "BD#F#G#": "G#m7",
    "ACEG": "Am7", "A#C#FG#": "A#m7", "ABDF#": "Bm7",

    # ディミニッシュ
    "CD#F#": "Cdm", "C#EG": "C#dm", "DFG#": "Ddm",
    "AF#D#": "D#dm", "A#GE": "Edm", "BG#F": "Fdm",
    "ACF#": "F#dm", "A#C#G": "Gdm", "BDG#": "G#dm",
    "ACD#": "Adm", "A#C#E": "A#dm", "BDF": "Bdm",
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
    """ピッチをキーに変換"""
    return PITCH[pitch]


def key_to_chord(key: str = None) -> str:
    """キーからコードに変換"""
    try:
        return CHORD[key]
    except KeyError:
        return key


def pitch_to_chord(pitches: list = None):
    """ピッチからコードに変換"""
    key = []
    for pitch in pitches:
        key.append(pitch_to_key(pitch))
    key = list(set(key))
    key.sort()
    return key_to_chord("".join(key))


def chord_to_value(key: str = None, stroke: bool = False) -> int:
    """コードに対応させてある値を返す"""
    chord = key_to_chord(key)
    if chord == 0:
        return 1
    if stroke:
        return KEY[chord] + 3
    return KEY[chord] + 1


if __name__ == "__main__":
    pass
