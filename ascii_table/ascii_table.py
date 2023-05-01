#!/usr/bin/env python3
import argparse

uart_ascii = {
    'a' : 'LHLLLLHHLH', # 0x61
    'b' : 'LLHLLLHHLH', # 0x62
    'c' : 'LHHLLLHHLH', # 0x63
    'd' : 'LLLHLLHHLH', # 0x64
    'e' : 'LHLHLLHHLH', # 0x65
    'f' : 'LLHHLLHHLH', # 0x66
    'g' : 'LHHHLLHHLH', # 0x67
    'h' : 'LLLLHLHHLH', # 0x68
    'i' : 'LHLLHLHHLH', # 0x69
    'j' : 'LLHLHLHHLH', # 0x6A
    'k' : 'LHHLHLHHLH', # 0x6B
    'l' : 'LLLHHLHHLH', # 0x6C
    'm' : 'LHLHHLHHLH', # 0x6D
    'n' : 'LLHHHLHHLH', # 0x6E
    'o' : 'LHHHHLHHLH', # 0x6F
    'p' : 'LLLLLHHHLH', # 0x70
    'q' : 'LHLLLHHHLH', # 0x71
    'r' : 'LLHLLHHHLH', # 0x72
    's' : 'LHHLLHHHLH', # 0x73
    't' : 'LLLHLHHHLH', # 0x74
    'u' : 'LHLHLHHHLH', # 0x75
    'v' : 'LLHHLHHHLH', # 0x76
    'w' : 'LHHHLHHHLH', # 0x77
    'x' : 'LLLLHHHHLH', # 0x78
    'y' : 'LHLLHHHHLH', # 0x79
    'z' : 'LLHLHHHHLH', # 0x7A
    ' ' : 'LLLLLLLHLH', # 0x40
    ',' : 'LLHLLLLHHH', # 0x2C
    '~' : 'HHHHHHHHHH', # idle
}



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "description goes here")
    parser.add_argument("--message", type=str, help = "set message [a-z,' ']", required=False)
    args = parser.parse_args()

    msg = ''
    res = 'HHH'

    if args.message:
        msg = args.message
        print ("message = ", msg)
    
    for s in list(msg):
        res = res + uart_ascii[s]

    res = res + 'HHH'


    if False:
        print (res.replace("L", "_").replace("H","~"))

    #print (res.replace("L", "👇").replace("H","👆"))    
    print (res.replace("L", "🙇").replace("H","🖐"))    

