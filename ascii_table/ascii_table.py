#!/usr/bin/env python3
import argparse

uart_ascii = {
    'a' : '__~~________~~~~__~~', # 0x61
    'b' : '____~~______~~~~__~~', # 0x62
    'c' : '__~~~~______~~~~__~~', # 0x63
    'd' : '______~~____~~~~__~~', # 0x64
    'e' : '__~~__~~____~~~~__~~', # 0x65
    'f' : '____~~~~____~~~~__~~', # 0x66
    'g' : '__~~~~~~____~~~~__~~', # 0x67
    'h' : '________~~__~~~~__~~', # 0x68
    'i' : '__~~____~~__~~~~__~~', # 0x69
    'j' : '____~~__~~__~~~~__~~', # 0x6A
    'k' : '__~~~~__~~__~~~~__~~', # 0x6B
    'l' : '______~~~~__~~~~__~~', # 0x6C
    'm' : '__~~__~~~~__~~~~__~~', # 0x6D
    'n' : '____~~~~~~__~~~~__~~', # 0x6E
    'o' : '__~~~~~~~~__~~~~__~~', # 0x6F
    'p' : '__________~~~~~~__~~', # 0x70
    'q' : '__~~______~~~~~~__~~', # 0x71
    'r' : '____~~____~~~~~~__~~', # 0x72
    's' : '__~~~~____~~~~~~__~~', # 0x73
    't' : '______~~__~~~~~~__~~', # 0x74
    'u' : '__~~__~~__~~~~~~__~~', # 0x75
    'v' : '____~~~~__~~~~~~__~~', # 0x76
    'w' : '__~~~~~~__~~~~~~__~~', # 0x77
    'x' : '________~~~~~~~~__~~', # 0x78
    'y' : '__~~____~~~~~~~~__~~', # 0x79
    'z' : '____~~__~~~~~~~~__~~', # 0x7A
    ' ' : '______________~~__~~', # 0x40
    ',' : '____~~________~~~~~~', # 0x2C
    '~' : '~~~~~~~~~~~~~~~~~~~~', # idle
}

1100

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "description goes here")
    parser.add_argument("--message", type=str, help = "set message [a-z,' ']", required=False)
    args = parser.parse_args()

    msg = ''

    if args.message:
        msg = args.message
        print ("message = ", msg)
    
    print ('~~~~', end='')

    for s in list(msg):
        print(uart_ascii[s], end='')

    print ('~~~~')

