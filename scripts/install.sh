#! /bin/bash
yes | sudo apt update 
yes | sudo apt upgrade -y
yes | sudo apt install bluetooth libusb-dev libdbus-1-dev \
libglib2.0-dev libudev-dev libical-dev libreadline-dev \
libdbus-glib-1-dev libbluetooth-dev
wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.54.tar.xz
tar Jxfv bluez-5.54.tar.xz
cd ./bluez-5.54/ || exit
./configure --enable-experimental
make -j "$(nproc)"
yes | sudo make install
cd ../
sudo pip3 install pybluez
rm -rf bluez-5.54
rm -rf bluez-5.54.tar.xz
pip3 install pretty_midi
