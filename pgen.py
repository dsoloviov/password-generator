#!/usr/bin/env python

from src.worker import generatePassword
from src.worker import checkLength
from src.worker import checkOptions
import argparse


def password(length=None, params=[]):
    parser = argparse.ArgumentParser(description='Generate password.')
    parser.add_argument('-L', '--length', help='length of the password')
    parser.add_argument('-d', '--digits', action='store_true', 
                        help='include digits')
    parser.add_argument('-l', '--lowercase', action='store_true', 
                        help='include lowercase characters')
    parser.add_argument('-u', '--uppercase', action='store_true', 
                        help='include uppercase characters')
    parser.add_argument('-s', '--special', action='store_true', 
                        help='include special characters')

    args = parser.parse_args()
    
    if args.length: length = args.length
    if args.digits: params.append('digits')
    if args.lowercase: params.append('lowercase')
    if args.uppercase: params.append('uppercase')
    if args.special: params.append('punctuation')

    return generatePassword(checkLength(length), checkOptions(params))


if __name__ == '__main__':
    print(password())
