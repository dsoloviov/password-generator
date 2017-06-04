#!/usr/bin/env python

import argparse
from src.charpas import CharPassword
from src.wordspas import WordsPassword


def password():
    parser = argparse.ArgumentParser(description='Generate password')
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-w", "--words", action="store_true", help='password consists of words')
    group.add_argument("-c", "--characters", action="store_true", help='password consists of characters')

    args = parser.parse_args()

    if args.words:
        wp = WordsPassword(complicate=True)
        print wp.password

    elif args.characters:
        cp = CharPassword()
        print cp.password


if __name__ == '__main__':
    password()
