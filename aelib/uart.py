#!/usr/bin/env python3
#Time-stamp: <2023-05-08 00:19:21 hamada>

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

def readFileBin(filename = '__dump__.img'):
    with open(filename, mode='rb') as f:
        _content = f.read() # list of Integers, not Bytes !
    print ('file: %s, size: %d-bytes' % (filename, len(_content)))

    # conversion: int -> byte
    _array_bytes = []
    for _ci in _content:
        _array_bytes.append(bytes([_ci]))

    return _array_bytes

def writeFileBin(filename = 'tmp.img', data = []):
    with open(filename, mode='wb') as f:
        for cb in data:
            f.write(cb)

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

    def testTx_binfiletransfer(self, filename = '/tmp/tran.img'):
        data_tx = readFileBin(filename = filename)

        n_byte = len(data_tx)
        progress_tick = int(n_byte / 20)

        for i, _b in enumerate(data_tx):
            self.uart_device.write(_b)
            if 0 == (i % progress_tick):
                print('=>', end='', flush=True)

        print("\n: End UART-Tx")

    def testRx_binfiletransfer(self, filename = '/tmp/recv.img', n_byte = 1048576):
        progress_tick = int(n_byte / 20)
        data_rx = []
        data_rx_byte = []
        for i in range(n_byte):
            rx_byte = self.uart_device.read(1)
            rx_int = struct.unpack('1B', rx_byte)[0]
            data_rx.append(rx_int)
            data_rx_byte.append(rx_byte)

            if 0 == i % progress_tick:
                print ('=>', end = '', flush = True)

        writeFileBin(filename = filename, data = data_rx_byte)

        print("\n: End UART-Rx")



    def diag(self):
        pprint.pprint(vars(self))
        return vars(self)
