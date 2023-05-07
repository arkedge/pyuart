#!/usr/bin/env python3
#Time-stamp: <2023-05-08 00:17:07 hamada>

import time
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "A time estimation tool for UART data/file transters")
    parser.add_argument("--size", type=int, help = "set file size in MBytes", required=False)
    parser.add_argument("--baud", type=int, help = "set baudrate", required=False)
    args = parser.parse_args()

    size_mb = 1
    baudrate = 115200

    if args.size:
        size_mb = int(args.size)

    if args.baud:
        baudrate = int(args.baud)

    n_byte = 1024 * 1024 * size_mb

    bandwidth = baudrate / 10.0 # bytes/sec

    peak_sec = n_byte / bandwidth

    print ("Transfer size (Bytes) = ", n_byte)
    print ("Baudrate = ", baudrate)
    print ("Peak bandwidth (Bytes/sec) = ", bandwidth)
    print ("Peak transfer time (sec) = ", peak_sec)
    print ("Peak transfer time (min) = ", peak_sec/60.0)
    print ("Peak transfer time (hour) = ", peak_sec/(60.0*60.0))
    print ("=======================================================")

    fname = "/tmp/dump.%dM.img" % int(size_mb)
    print ("dd if=/dev/urandom of=%s bs=1024k count=%d" % (fname, size_mb))
    
