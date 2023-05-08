#!/usr/bin/env python3
#Time-stamp: <2023-05-08 00:17:07 hamada>

import time

from aelib import uart

if __name__ == '__main__':
    u0 = uart.uart(dev='/dev/ttyS0', baudrate = 115200, timeout = 240)
    u0.open()
    u0.diag()

    if False:
        u0.testRx_binfiletransfer(filename = './recv.img~', n_byte = 997)

    while True:
        rx_data = u0.rx()
        if True == rx_data['is_valid']:
            print ('0x%02X, %s' % (rx_data['int'], rx_data['byte']))
        else:
            time.sleep (1)
        
    u0.close()

