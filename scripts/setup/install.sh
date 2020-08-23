#! /bin/bash
yes | sudo apt update 
yes | sudo apt upgrade
yes | sudo apt install bluez bluetooth libusb-dev libdbus-1-dev \
libglib2.0-dev libudev-dev libical-dev libreadline-dev \
libdbus-glib-1-dev libbluetooth-dev 
pip3 install setuptools --user
pip3 install pandas pybluez pretty_midi --user