#! /bin/bash
yes | sudo apt update 
yes | sudo apt upgrade -y
yes | sudo install bluetooth
yes | sudo apt install libusb-dev
yes | sudo apt install libdbus-1-dev
yes | sudo apt install libglib2.0-dev
yes | sudo apt install libudev-dev
yes | sudo apt install libical-dev
yes | sudo apt install libreadline-dev
yes | sudo apt install libdbus-glib-1-dev
yes | sudo apt install libbluetooth-dev

cd ~/
wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.54.tar.xz

xz -dv bluez-5.54.tar.xz
tar -xf bluez-5.54.tar
cd bluez-5.54/
./configure --enable-experimental
make -j$(nproc)
yes | sudo make install
sudo pip3 install pybluez