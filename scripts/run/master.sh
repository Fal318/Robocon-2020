#!/bin/bash
sudo ntpdate -b 192.168.10.10
cd ../../master/
python3 main.py
