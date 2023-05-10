#!/usr/bin/env python3
#Time-stamp: <2023-05-10 09:58:58 hamada>

from mpi4py import MPI

if __name__ == '__main__':

    comm = MPI.COMM_WORLD
    proc_id = comm.Get_rank()
    nproc = comm.Get_size()
    hostname = MPI.Get_processor_name()

    devfile = "/dev/ttyUSB%d" % proc_id
    print(devfile, flush=True)


