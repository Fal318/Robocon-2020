# -*- coding: utf-8 -*-
import csv
import pretty_midi
import key

TARGET = 1000


def ins_to_list(ins: pretty_midi.containers.Note):
    return [ins.start, ins.end, ins.pitch, ins.velocity]


def writer_csv(arrs: list):
    with open('../server/data.csv', 'w') as f:
        writer = csv.writer(f)
        for arr in arrs:
            writer.writerows(arr)


def main():
    midi_data = None
    count = 0
    try:
        midi_data = pretty_midi.PrettyMIDI("../midi/robocon.mid")
    except:
        print("Error")
    inotes, chords = [], []
    for instrument in midi_data.instruments:
        print(instrument)#.program)
        if instrument.program == TARGET:
            count += 1
            inote = instrument.notes
            for ins in inote:
                if isinstance(type(ins), list):
                    continue
                else:
                    inotes.append(ins_to_list(ins))
        if count >= 2:
            break

    #inotes.sort()

    index= 0
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
            
        chord = key.pitch_to_chord(pitches)
        chords.append(chord)
        print(chord)
    
    return chords


if __name__ == '__main__':
    chord = main()
