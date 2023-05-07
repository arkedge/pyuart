#!/usr/bin/env python3
#Time-stamp: <2023-05-07 20:36:23 hamada>
import serial
import time
import pprint

def byte2int(i_byte, i_endian = 'big'):
    return int.from_bytes(i_byte, i_endian)

def int2byte(i_int, i_endian = 'big'):
    n_octet = math.ceil(math.log2(i_int)/8.0)
    print ("n_octet: %d" % n_octet)
    return i_int.to_bytes(n_octet, i_endian)

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
        'timeout': 10,
    }

    uart_device = serial.Serial(uart_settings['dev'], uart_settings['baudrate'], timeout=uart_settings['timeout'])

    cnt = 0
    while False:
        #str = uart_device.readline().strip().decode("utf-8")
        str = uart_device.readline().strip()
        print(type(str))
        print(str)
        time.sleep(0.1)
        cnt = cnt + 1


    n_byte = 1048576
    data_rx = uart_device.read(n_byte)
    print(type(data_rx))
    print(len(data_rx))

    uart_device.close()

