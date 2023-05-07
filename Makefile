TARGET=test.py

all:

run:
	./${TARGET}


gen.1M:
	dd if=/dev/urandom of=/tmp/dump.img bs=1024k count=1
	shasum -a 512 /tmp/dump.img

gen.8M:
	dd if=/dev/urandom of=/tmp/dump.img bs=1024k count=8
	shasum -a 512 /tmp/dump.img

gen.38M:
	dd if=/dev/urandom of=/tmp/dump.img bs=1024k count=38
	shasum -a 512 /tmp/dump.img

screen:
	screen /dev/ttyS0 115200

chmod: chmod.AMA0 chmod.S0

chmod.AMA0:
	sudo chmod 666 /dev/ttyAMA0

chmod.S0:
	sudo chmod 666 /dev/ttyS0

chmod.USB0:
	sudo chmod 666 /dev/ttyUSB0

setup:
	sudo apt remove brltty
	sudo pip3 install pyserial
	sudo pip3 install pyusb

