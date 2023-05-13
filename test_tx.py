#!/usr/bin/env python3
#Time-stamp: <2023-05-08 21:52:05 hamada>

import time

from aelib import uart

if __name__ == '__main__':
    u0 = uart.uart(dev='/dev/ttyUSB0', baudrate = 115200, timeout = 15)
    u0.open()
    u0.diag()

    # -----------------------------------------
    #  send data from 'a' to 'z' in ASCII code
    # -----------------------------------------
    for i in range(0x61, 0x7b):
        u0.tx(i)

    u0.close()

