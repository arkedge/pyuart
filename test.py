#!/usr/bin/env python3
#Time-stamp: <2023-05-05 00:54:04 hamada>

import time

from aelib import uart

if __name__ == '__main__':
    u0 = uart.uart()
    u0.open()
    u0.diag()

    while True:
        #data = 0x4675636b2075206675636b2075206675636b2075200D0A
        data = 0x6362610D0A
        u0.testTx(data)
        #time.sleep(0.777)

    u0.close()

