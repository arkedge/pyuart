#!/usr/bin/env python3


def gen_bram_data():

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


    return bram



if __name__ == "__main__":

    bram = gen_bram_data()

    xstr = ''
    for xi in bram:
        xstr = xstr + '%02x ' % (xi)

    msg = ""
    msg = msg + "memory_initialization_radix=16;\n"
    msg = msg + "memory_initialization_vector = "
    msg = msg + xstr
    msg = msg + ";\n"
    print (msg)

