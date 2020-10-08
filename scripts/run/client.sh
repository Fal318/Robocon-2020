#!/bin/bash
sudo ntpdate -b 192.168.10.10
name=$HOSTNAME
cd ../../client
if [ $name == "ukulele" ]; then
    python3 client_u.py
elif [ $name == "percussion" ]; then
    python3 client_p.py
fi
