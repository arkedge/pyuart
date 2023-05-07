#!/usr/bin/env python3
#Time-stamp: <2023-05-03 14:19:31 hamada>

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
    'dev': '/dev/ttyS0', #'/dev/ttyUSB0',
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

'''????
bbb = binascii.b2a_hex(b'm') # b'6d'
bbx = byte2int(bbb) # 0x3664
print(bbb)
print('0x%x' % bbx)
data = byte2int(binascii.b2a_hex(b'abcdef'), byte_order)
print ("0x%x"%data)
'''

#data = 0xdeadbeaf
#data = 0x31415926535897932384
#data = 0x314159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808

#data = 0x6675636b4075 # fuck u
data = 0x610D0A # A<CR><LF>
data = 0x6675636b40750D0A # A<CR><LF>
#data = data.to_bytes(n_octet, byte_order)
data = 0x6675636b20750D0A # fuck u<CR><LF>
data = 0x61
data = 0x4675636b2075206675636b2075206675636b2075200D0A

cnt = 0

b = [0x61, 0x62, 0x63, 0x0D, 0x0A]

while True:
    data_byte = int2byte(data, byte_order)
    #data_byte = binascii.hexlify(b"hello\n")
    data_byte = bytes(b)
    uart_device.write(data_byte)
    print("0x%x" % byte2int(data_byte, byte_order))
    print("len=%d" % len(data_byte))
    time.sleep(1.0)
    cnt = cnt + 1
    '''
    data = data + 1
    if data > 0x7d00:
        data = 0x6101
    '''

uart_device.close()


