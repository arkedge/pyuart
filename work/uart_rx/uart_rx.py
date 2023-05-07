#!/usr/bin/env python3
#Time-stamp: <2023-05-08 00:13:13 hamada>
import struct
import serial
import time
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
        print('====================')
        print(_b)
        print(type(_b))
        print(len(_b))
        _x = struct.unpack('1B', _b)
        array_int.append(_x[0])
    return array_int


def readFileBin(filename = 'dump.1M.img'):
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


def testReadWriteBin():
    content = readFileBin()
    writeFileBin('tmp3.img', data = content)


if __name__ == '__main__':
    byte_order = 'big'

    uart_settings = {
        'dev': '/dev/ttyUSB0',#'/dev/ttyS0', #'/dev/ttyAMA0',
        'baudrate': 115200, #9600, # 9600, 115200
        'timeout': 30,
    }

    uart_device = serial.Serial(uart_settings['dev'], uart_settings['baudrate'], timeout=uart_settings['timeout'])

    '''
    cnt = 0
    while False:
        #str = uart_device.readline().strip().decode("utf-8")
        str = uart_device.readline().strip()
        print(type(str))
        print(str)
        time.sleep(0.1)
        cnt = cnt + 1
    '''

    #n_byte = 1073741824 # 1GB
    #n_byte = 8388608 # 8MB ... ~ 12m+20sec
    n_byte = 1048576 # 1MB
    n_byte = 39845888 # 38MB ... ~ 1 hour
    progress_tick = int(n_byte / 20)
    data_rx = []
    data_rx_byte = []
    for i in range(n_byte):
        rx_byte = uart_device.read(1)
        rx_int = struct.unpack('1B', rx_byte)[0]
        data_rx.append(rx_int)
        data_rx_byte.append(rx_byte)

        if 0 == i % progress_tick:
            print ('=>', end='', flush=True)


    writeFileBin(filename='tmp2.img', data=data_rx_byte)

    '''
    print(type(data_rx))
    print(len(data_rx))
    '''
    '''
    for i, d in enumerate(data_rx):
        print ('%d: 0x%X' % (i, d))
    '''

    print('End UART-Rx')
    uart_device.close()

