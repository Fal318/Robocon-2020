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
wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.54.tar.xz
tar Jxfv bluez-5.54.tar.xz
cd bluez-5.54/
./configure --enable-experimental
make -j$(nproc)
yes | sudo make install
cd ../
sudo pip3 install pybluez
rm -rf bluez-5.54
rm -rf bluez-5.54.tar.xz