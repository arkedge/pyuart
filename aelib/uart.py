#!/usr/bin/env python3
#Time-stamp: <2023-05-03 15:44:13 hamada>

__author__ = "Tsuyoshi Hamada <hamada@arkedgespace.com>"

import serial
import time
import math
import binascii
import pprint


def byte2int(i_byte, i_endian = 'big'):
    return int.from_bytes(i_byte, i_endian)

def int2byte(i_int, i_endian = 'big'):
    n_octet = math.ceil(math.log2(i_int)/8.0)
    print ("n_octet: %d" % n_octet)
    return i_int.to_bytes(n_octet, i_endian)

byte_order = 'big'

uart_settings = {
    'dev': '/dev/ttyUSB0',
    'baudrate': 115200, #9600, # 9600, 115200
    'timeout': 10,
    }

class uart:

    def __init__(self, dev=uart_settings['dev'], baudrate=uart_settings['baudrate'], timeout=uart_settings['timeout'], byte_order=byte_order):
        self.dev = dev
        self.baudrate = baudrate
        self.timeout = timeout
        self.byte_order = byte_order

    def open(self):
        self.uart_device = serial.Serial(self.dev, self.baudrate, timeout=self.timeout)

    def close(self):
        self.uart_device.close()

    def testTx(self, data=0x6162636465666768696a6b6c6d6e6f707172737475767778797a):
        data = data << 16 | 0x0D0A # <CR><LF>
        data_byte = int2byte(data, byte_order)
        self.uart_device.write(data_byte)
        print("0x%x" % byte2int(data_byte, byte_order))
        time.sleep(1.0)

    def diag(self):
        pprint.pprint(vars(self))
        return vars(self)
