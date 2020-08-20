# -*- coding: utf-8 -*-
"""MIDIを楽器ごとのCSVに変換する"""
import pandas as pd
import pretty_midi
import key

SONG_TIME: int = 2550


def ins_to_list(ins: pretty_midi.containers.Note):
    """MIDIデータ(ノート)から必要なものだけ取り出す"""
    return [ins.start, ins.end, ins.pitch, ins.velocity]


def writer_csv(arrs: list, ins_num: int):
    """データフレームをCSVに書き出し"""
    pd.Series(arrs).to_csv(
        f"../../data/csv/data_{ins_num}.csv", header=False, index=False)


def fix_arrays(arrs: list):
    """配列を使いやすい形に変換"""
    fixed_arrays = [None for _ in range(SONG_TIME)]
    arrs.sort(key=lambda x: x[0][0])
    while len(arrs) > 0:
        arr = arrs.pop(0)
        start, stop = int(arr[0][0]), int(arr[0][1])
        for index in range(start, stop):
            fixed_arrays[index] = arr[1]
    return fixed_arrays


def main(ins_num):
    """メイン"""
    midi_data = None
    inotes, chords = [], []
    midi_data = pretty_midi.PrettyMIDI("../../data/midi/robocon.mid")
    for instrument in midi_data.instruments:
        if instrument.program == ins_num:
            inote = instrument.notes
            for ins in inote:
                if not isinstance(type(ins), list):
                    inotes.append(ins_to_list(ins))
                else:
                    continue

    index = 0
    while index < len(inotes)-1:
        pitches = [inotes[index][2]]

        while index < len(inotes)-1:
            if inotes[index][0] == inotes[index+1][0]:
                if inotes[index][1] == inotes[index+1][1]:
                    pitches.append(inotes[index+1][2])
                    index += 1
                else:
                    index += 1
                    break
            else:
                index += 1
                break
        start = inotes[index][0]*10
        stop = inotes[index][1]*10
        chords.append([[start, stop], key.pitch_to_chord(pitches)])
    if len(chords) == 0:
        return None
    return chords


if __name__ == '__main__':
    for i in range(129):
        chord = main(i)
        if chord is not None:
            farry = fix_arrays(chord)
            writer_csv(farry, i)
