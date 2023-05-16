#!/usr/bin/env python3
#Time-stamp: <2023-05-16 10:45:22 hamada>

from aelib import uart

if __name__ == '__main__':
    u0 = uart.uart(dev='/dev/ttyUSB0', baudrate = 115200, timeout = 240)
    u0.open()
    u0.diag()

    for v in u0.rx():
        print ('0x%02X' % (v), flush=True)

    u0.close()

