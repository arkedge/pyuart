#!/usr/bin/env python3
#Time-stamp: <2023-05-03 15:24:55 hamada>

import time
import math
import binascii

from aelib import uart


'''
class uart:

    def __init__(self, dev=uart_settings['dev'], baudrate=uart_settings['baudrate'], timeout=uart_settings['timeout'], byte_order=byte_order):
        self.dev = dev
        self.baudrate = baudrate
        self.timeout = timeout
        self.byte_order = byte_order

    def open(self):
        self.uart_device = serial.Serial(self.dev, self.baudrate, self.timeout)

    def close(self):
        self.uart_device.close()

    def testTx(self):
        data = 0x6675636b20750D0A # fuck u<CR><LF>
        data_byte = int2byte(data, byte_order)
        self.uart_device.write(data_byte)
        print("0x%x" % byte2int(data_byte, byte_order))
        time.sleep(1.0)

'''

if __name__ == '__main__':
    u0 = uart.uart()
    u0.open()
    u0.diag()
    while True:
        u0.testTx()
        time.sleep(1)


    u0.close()
