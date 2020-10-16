"""key.py"""
# -*- coding: utf-8 -*-
import numpy as np


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


if __name__ == "__main__":
    pass
