#!/usr/bin/env python3
#Time-stamp: <2023-05-05 16:22:28 hamada>

__author__ = "Tsuyoshi Hamada <hamada@arkedgespace.com>"

import struct
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

'''
array conversion: int -> byte
    array is list in python
'''
def convArrayInt2Byte(array_int):
    array_byte = []
    for data_i in array_int:
        array_byte.append(bytes([0xff & data_i]))
    return array_byte

'''
array conversion: byte -> int
    array is list in python
'''
def convArrayByte2Int(array_byte):
    array_int = []
    for _b in array_byte:
        _x = struct.unpack('1B', _b)
        array_int.append(_x[0])
    return array_int

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
        _eot = 0x04
        data = data << 16 | 0x0D0A # <CR><LF>
        data = 0x6465
        data_byte = int2byte(data, byte_order)
        self.uart_device.write(data_byte)
        if False:
            print("0x%x" % byte2int(data_byte, byte_order))
            time.sleep(1.0)

    def testTx512octet(self):
        n_byte = 10 # 512
        msg_i = []
        for i in range(n_byte):
            msg_i.append(i)

        msg_ba = convArrayInt2Byte(msg_i)

        for _b in msg_ba:
            self.uart_device.write(_b)

        print("----------------")
        '''
        msg_i2 = convArrayByte2Int(msg_ba)
        pprint.pprint(msg_i)
        pprint.pprint(msg_ba)
        pprint.pprint(msg_i2)
        '''

        time.sleep(5)

    def diag(self):
        pprint.pprint(vars(self))
        return vars(self)
