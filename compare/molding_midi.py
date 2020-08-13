import pretty_midi

target = 6

midi_data = pretty_midi.PrettyMIDI("../midi/kanon.mid")
ins = pretty_midi.instrument.Instrument
for instrument in midi_data.instruments:
    if instrument.program == target:
        ins = instrument

for i in ins.notes:
    print(pretty_midi.note_number_to_name(i.pitch))
rev_en_chord = pretty_midi.PrettyMIDI()
rev_en_chord.instruments.append(ins)
rev_en_chord.write(f'../midi/ins_{target}.mid')
