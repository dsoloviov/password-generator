#!/usr/bin/env python

import sys
from random import randint as r
from src.basicPassword import BasicPassword


def generate_password():
    def options_constructor():
        if '--all' in sys.argv:
            return False
    print(sys.argv)
    p = BasicPassword(1, 10, options_constructor())
    return p.get_password()


def password(number, length, params=False):
    p = BasicPassword(number, length, params)
    return p.get_password()


if __name__ == '__main__':
    print(generate_password())
