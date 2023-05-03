#!/usr/bin/env python3
#Time-stamp: <2023-05-03 15:59:51 hamada>

import time

from aelib import uart

if __name__ == '__main__':
    u0 = uart.uart()
    u0.open()
    u0.diag()

    while True:
        u0.testTx()
        time.sleep(0.777)

    u0.close()

