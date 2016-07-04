#!/usr/bin/env python

import sys
from random import randint as r
from src.worker import generatePassword
from src.worker import checkLength

LENGTH = 10


def getpsw(length=LENGTH, params=[]):
    params_mapper = {'-d': 'digits', '-l': 'lowercase',
                     '-u': 'uppercase', '-s': 'punctuation'}
    for key, value in params_mapper.iteritems():
        if key in sys.argv:
            params.append(value)
    if '-L' in sys.argv:
        try:
            length = checkLength(sys.argv[sys.argv.index('-L') + 1])
        except IndexError:
            length = LENGTH
    if length <= 0:
        length = LENGTH
    return generatePassword(length, params)


if __name__ == '__main__':
    password = getpsw()
    print('\n')
    print password
    print('\n')
