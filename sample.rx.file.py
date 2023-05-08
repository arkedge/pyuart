#!/usr/bin/env python3
#Time-stamp: <2023-05-08 21:39:05 hamada>

import time

from aelib import uart

if __name__ == '__main__':
    u0 = uart.uart(dev='/dev/ttyUSB0', baudrate = 115200, timeout = 240)
    u0.open()
    u0.diag()

    u0.rx_file(filename = './recv.img', n_byte = 1048576)

    u0.close()

