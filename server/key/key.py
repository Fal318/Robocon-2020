"""key.py"""
# -*- coding: utf-8 -*-
KEY = {
    "C": {
        "O": 0, "Om": 12, "O7": 24, "Om7": 36, "Odm": 48
    },
    "CS": {
        "O": 1, "Om": 13, "O7": 25, "Om7": 37, "Odm": 49
    },
    "D": {
        "O": 2, "Om": 14, "O7": 26, "Om7": 38, "Odm": 50
    },
    "DS": {
        "O": 3, "Om": 15, "O7": 27, "Om7": 39, "Odm": 51
    },
    "E": {
        "O": 4, "Om": 16, "O7": 28, "Om7": 40, "Odm": 52
    },
    "F": {
        "O": 5, "Om": 17, "O7": 29, "Om7": 41, "Odm": 53
    },
    "FS": {
        "O": 6, "Om": 18, "O7": 30, "Om7": 42, "Odm": 54
    },
    "G": {
        "O": 7, "Om": 19, "O7": 31, "Om7": 43, "Odm": 55
    },
    "GS": {
        "O": 8, "Om": 20, "O7": 32, "Om7": 44, "Odm": 56
    },
    "A": {
        "O": 9, "Om": 21, "O7": 33, "Om7": 45, "Odm": 57
    },
    "AS": {
        "O": 10, "Om": 22, "O7": 34, "Om7": 46, "Odm": 58
    },
    "B": {
        "O": 11, "Om": 23, "O7": 35, "Om7": 47, "Odm": 59
    },
}

if __name__ == "__main__":
    value = []
    for key in KEY:
        for k in KEY[key].keys():
            value.append(KEY[key][k])
    if len(value) != len(list(set(value))):
        print("重複あり")
    else:
        print("重複なし")
