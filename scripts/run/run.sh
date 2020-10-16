#!/bin/bash
name=$HOSTNAME
if [ $name == "laptop" ]; then
    cd ../../master
    python3 master.py
else
    sudo ntpdate -b 192.168.10.5
    if [ $name == "ukulele" ]; then
        cd ../../client
        python3 client_u.py
    elif [ $name == "percussion" ]; then
        cd ../../client
        python3 client_p.py
    fi
fi
