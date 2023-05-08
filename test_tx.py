#!/usr/bin/env python3
#Time-stamp: <2023-05-08 21:08:46 hamada>

import time

from aelib import uart

if __name__ == '__main__':
    u0 = uart.uart(dev='/dev/ttyUSB0', baudrate = 115200, timeout = 15)
    u0.open()
    u0.diag()

    u0.tx_file(filename = '/tmp/dump.400M.img')

    u0.close()

