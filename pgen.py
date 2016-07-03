#!/usr/bin/env python

import sys
from random import randint as r
from src.basicPassword import BasicPassword


def generate_password():
    def get_params():
        params = []
        number = 1
        length = 10
        params_mapper = {'-d': 'digits', '-l': 'lowercase',
                          '-u': 'uppercase', '-s': 'punctuation'}
        for key, value in params_mapper.iteritems():
            if key in sys.argv:
                params.append(value)
        if '-N' in sys.argv:
            number = sys.argv[sys.argv.index('-N') + 1]
        if '-L' in sys.argv:
            length = sys.argv[sys.argv.index('-L') + 1]
        return [int(number), int(length), params]

    number, length, params = get_params()
    p = BasicPassword(number, length, params)
    return p.get_password()


def password(number, length, params=False):
    p = BasicPassword(number, length, params)
    return p.get_password()


if __name__ == '__main__':
    passwords = generate_password()
    print('\n')
    for each in passwords: print each
    print('\n')
