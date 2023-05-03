#!/usr/bin/env python3
#Time-stamp: <2023-04-30 19:47:01 hamada>
import serial
import time


def byte2int(i_byte, i_endian = 'big'):
    return int.from_bytes(i_byte, i_endian)

def int2byte(i_int, i_endian = 'big'):
    n_octet = math.ceil(math.log2(i_int)/8.0)
    print ("n_octet: %d" % n_octet)
    return i_int.to_bytes(n_octet, i_endian)

byte_order = 'big'

uart_settings = {
    'dev': '/dev/ttyS0', #'/dev/ttyAMA0',
    'baudrate': 115200, #9600, # 9600, 115200
    'timeout': 10,
    }

uart_device = serial.Serial(uart_settings['dev'], uart_settings['baudrate'], timeout=uart_settings['timeout'])

cnt = 0
while True:
    str = uart_device.readline().strip().decode("utf-8")
    #str = uart_device.readline()
    print(str)
    time.sleep(0.1)
    cnt = cnt + 1

uart_device.close()

