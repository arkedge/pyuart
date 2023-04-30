#!/usr/bin/env python3
#Time-stamp: <2023-04-30 19:28:57 hamada>

import serial
import time
import math
import binascii


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

uart_device = serial.Serial(uart_settings['dev'], uart_settings['baudrate'], timeout=uart_settings['timeout'])

#data = 0b10101010
#data = 0b1010101010101010
#data = 0x123456789abcdef0123456789abcdef0
#data = 0b11000100
#data = 0b00110010
#data = 0x321

bbb = binascii.b2a_hex(b'm') # b'6d'
bbx = byte2int(bbb) # 0x3664
print(bbb)
print('0x%x' % bbx)
data = byte2int(binascii.b2a_hex(b'abcdef'), byte_order)
print ("0x%x"%data)

#data = 0xdeadbeaf
#data = 0x31415926535897932384
#data = 0x314159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808

time.sleep(1)

#data = data.to_bytes(n_octet, byte_order)

cnt = 0
while True:
    data_byte = int2byte(data, byte_order)
    uart_device.write(data_byte)
    print("0x%x" % byte2int(data_byte, byte_order))
    time.sleep(1.0)
    cnt = cnt + 1

uart_device.close()


# F@@@@@@@CK
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!
# I want to change this from python to RUST !!!!!!

