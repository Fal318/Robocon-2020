# -*- coding: utf-8 -*-
"""MIDIを楽器ごとのCSVに変換する"""
import math
import pandas as pd
import pretty_midi
import key


def get_longs(midi_data: pretty_midi.PrettyMIDI) -> int:
    """曲の長さ(ms)を返す"""
    songs_long = 0
    for instrument in midi_data.instruments:
        for note in instrument.notes:
            end = note.end
            if end > songs_long:
                songs_long = end
    songs_long = int(math.ceil(songs_long))*10
    return songs_long


def ins_to_list(ins: pretty_midi.containers.Note) -> list:
    """MIDIデータ(ノート)から必要なものだけ取り出す"""
    return [ins.start, ins.end, ins.pitch, ins.velocity]


def writer_csv(arrs: list, ins_num: int):
    """データフレームをCSVに書き出し"""
    used_num = [33, 113, 116, 122]
    if ins_num in used_num:
        pd.Series(arrs).to_csv(
            f"../../data/csv/data_{ins_num}.csv", header=False, index=False)


def fix_arrays(arrs: list, time_length: int) -> list:
    """配列を使いやすい形に変換"""
    fixed_arrays = ["" for _ in range(time_length)]
    arrs.sort(key=lambda x: x[0][0])
    while len(arrs) > 0:
        arr = arrs.pop(0)
        start, stop = int(arr[0][0]), int(arr[0][1])
        for index in range(start, stop):
            fixed_arrays[index] = arr[1]
    return fixed_arrays


def main(ins_num) -> list:
    """メイン"""
    inotes, chords = [], []
    midi_data = pretty_midi.PrettyMIDI("../../data/midi/robocon.mid")
    song_long = get_longs(midi_data)
    for instrument in midi_data.instruments:
        if instrument.program == ins_num:
            inote = instrument.notes
            for ins in inote:
                if not isinstance(type(ins), list):
                    inotes.append(ins_to_list(ins))

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
        return [None, None]
    return [chords, song_long]


if __name__ == '__main__':
    for i in range(129):
        chord, long = main(i)
        if chord is not None:
            farry = fix_arrays(chord, long)
            writer_csv(farry, i)
