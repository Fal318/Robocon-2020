#!/bin/bash
sudo ntpdate -b 192.168.10.10
name=$HOSTNAME
if [ $name == "ukulele" ]; then
    cd ../../client
    python3 client_u.py
elif [ $name == "percussion" ]; then
    cd ../../client
    python3 client_p.py
elif [ $name == "laptop" ]; then
    cd ../../master
    python3 main.py
fi
