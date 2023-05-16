#!/usr/bin/env python3

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

    while True:
        for i in range(0x100):
            u0.tx(i)
        

    u0.close()
    
