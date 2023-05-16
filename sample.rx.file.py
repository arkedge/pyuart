#!/usr/bin/env python3

from aelib import uart

if __name__ == '__main__':
    u0 = uart.uart(dev='/dev/ttyUSB0', baudrate = 115200, timeout = 240)
    u0.open()
    u0.diag()

    file_size = 0x1 << 20 #   1 MB
    file_size = 0x1 << 28 # 256 MB

    u0.rx_file(filename = './recv.img', n_byte = file_size)

    u0.close()

