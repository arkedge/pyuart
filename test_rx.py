#!/usr/bin/env python3
#Time-stamp: <2023-05-08 00:17:07 hamada>

import time

from aelib import uart

if __name__ == '__main__':
    u0 = uart.uart(dev='/dev/ttyS0', baudrate = 115200, timeout = 20)
    u0.open()
    u0.diag()

    u0.testRx_binfiletransfer(filename = '/tmp/recv__.img', n_byte = 1048576)

    u0.close()

