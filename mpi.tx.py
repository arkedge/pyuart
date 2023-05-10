#!/usr/bin/env python3
#Time-stamp: <2023-05-10 09:58:58 hamada>

import time
from mpi4py import MPI
from aelib import uart

if __name__ == '__main__':

    comm = MPI.COMM_WORLD
    proc_id = comm.Get_rank()
    nproc = comm.Get_size()
    hostname = MPI.Get_processor_name()

    devfile = "/dev/ttyUSB%d" % proc_id
    print(devfile, flush=True)

    u0 = uart.uart(dev=devfile, baudrate = 115200, timeout = 15)
    u0.open()
    for i in range(0x100000):
        v = 0xFF & (0x1 << i % 9)
        v = 0x0
        print ("0x%02X" % v)
        for j in range(0x4000):
            u0.tx(v)

    u0.close()
    
