#!/usr/bin/env python3

from aelib import uart

if __name__ == '__main__':
    u0 = uart.uart(dev='/dev/ttyUSB0', baudrate = 115200, timeout = 240)
    u0.open()
    u0.diag()

    for v in u0.rx():
        print ('%02X ' % (v), flush=True, end='')

    u0.close()

