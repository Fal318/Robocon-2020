#!/bin/bash
sudo ntpdate -b ntp.nict.jp
cd ../../master/
python3 main.py -d
