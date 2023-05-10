#!/usr/bin/env python3
#Time-stamp: <2023-05-10 09:37:27 hamada>

from mpi4py import MPI

if __name__ == '__main__':

    comm = MPI.COMM_WORLD
    proc_id = comm.Get_rank()
    nproc = comm.Get_size()
    hostname = MPI.Get_processor_name()

    #print(f"{hostname}: {nproc}: {proc_id}", flush=True)
    print("{0}, {1}/{2}".format(hostname, proc_id, nproc), flush=True)


