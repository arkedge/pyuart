#!/usr/bin/env python3

from aelib import uart

if __name__ == '__main__':
    u0 = uart.uart(dev='/dev/ttyUSB0', baudrate = 115200, timeout = 15)
    u0.open()
    u0.diag()
    print (uart.get_baudrate_list())

    res = u0.tx_file(filename = './dump.256M.img')
    print (res)

    u0.close()

