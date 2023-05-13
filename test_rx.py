#!/usr/bin/env python3
#Time-stamp: <2023-05-11 16:47:18 hamada>

import time

from aelib import uart



if __name__ == '__main__':
    u0 = uart.uart(dev='/dev/ttyUSB0', baudrate = 115200, timeout = 240)
    u0.open()
    u0.diag()

    for v in u0.rx_generator():
        print ('0x%02X' % (v), flush=True)

    u0.close()

