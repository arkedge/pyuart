TARGET=uart_rx.py

all:

run:
	./${TARGET}


gen:
	dd if=/dev/urandom of=dump.1M.img bs=1024 count=1024
	shasum -a 512 *.img

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

