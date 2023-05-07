#!/usr/bin/env python3
#Time-stamp: <2023-05-05 00:54:04 hamada>

import time

from aelib import uart

if __name__ == '__main__':
    u0 = uart.uart(dev='/dev/ttyS0', baudrate = 115200, timeout = 15)
    u0.open()
    u0.diag()

    u0.testTx_binfiletransfer(filename = '/tmp/dump.1M.img')

    u0.close()

