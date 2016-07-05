#!/usr/bin/env python

from random import randint as simple_random
from re import findall
import string


def generatePassword(length, params):
    table = generateTable(params)
    limit = len(table)
    valid = False
    while(valid == False):
        password = ''.join([table[randomize(limit)] for x in range(length)])
        valid = bool(isValid(password, params))
    return password


def generateTable(options):
    table = []
    if options:
        for option in options:
            table += getattr(string, option)
    else:
        return dict(enumerate(string.digits +
                              string.lowercase +
                              string.uppercase +
                              string.punctuation))
    return dict(enumerate(table))


def randomize(limit):
    return simple_random(0, limit - 1)


def isValid(password, options):
    """
    Validates that password contains
    all necessary types of characters
    """
    mapper = {'digits': '0-9',
              'lowercase': 'a-z',
              'uppercase': 'A-Z',
              'punctuation': string.punctuation}
    if options:
        for option in options:
            if not findall('[%s]' % mapper[option], password):
                return False
    else:
        for key in mapper:
            if not findall('[%s]' % mapper[key], password):
                return False
    return True


def checkLength(length):
    try:
        length = int(length)
    except ValueError:
        length = 10
    finally:
        return length if length > 0 else 10

def checkOptions(options):
    standard = ['digits', 'lowercase', 'uppercase', 'punctuation']
    for option in options:
        if option not in standard:
            options.pop(options.index(option))
            checkOptions(options)  # recursion
    return options
