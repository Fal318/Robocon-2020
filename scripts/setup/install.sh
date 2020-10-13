#! /bin/bash
sudo apt update 
sudo apt upgrade -y
sudo apt install -y bluez bluetooth libbluetooth-dev 
libusb-dev libdbus-1-dev libglib2.0-dev libudev-dev \
libical-dev libreadline-dev libdbus-glib-1-dev  ntp ntpdate
pip3 install setuptools --user
pip3 install pandas pybluez pyserial --user