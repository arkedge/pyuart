#!/usr/bin/env python3



msg = ""
msg = msg + "memory_initialization_radix=16;\n"
msg = msg + "memory_initialization_vector = "

#01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f 20;

bram = []
for ch in range(16):
    for i in range(1024):
        x_L = 0xF & i
        x_H = (0xF & ch) << 4
        x = x_H | x_L
        if (ch>11):
            x = 0xff
        bram.append(x)


for i in range(1024):
    bram[i] = 0xff

xstr = ''
for xi in bram:
    xstr = xstr + '%02x ' % (xi)

msg = msg + xstr


msg = msg + ";\n"


print (msg)

