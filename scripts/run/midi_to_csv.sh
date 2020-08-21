#!/bin/bash
cd ../../server/library/
python3 midi_to_csv.py
python3 merge_csv.py
cd ../../data/csv/
rm ./data_*.csv