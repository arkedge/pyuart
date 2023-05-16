TARGET=test_tx.py

all:

run:
	./${TARGET}

mpirun:
	mpirun -np 4 --oversubscribe mpi.tx.py

gen.8M:
	dd if=/dev/urandom of=/tmp/dump.img bs=1024k count=8
	shasum -a 512 /tmp/dump.img

screen:
	screen /dev/ttyS0 115200

chmod:
	sudo chmod 666 --silent /dev/ttyUSB*
	sudo chmod 666 --silent /dev/ttyAMA0
	sudo chmod 666 --silent /dev/ttyS0


setup:
	sudo apt remove brltty
	sudo pip3 install pyserial
	sudo apt install python3-mpi4py
