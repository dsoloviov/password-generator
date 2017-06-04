#/usr/bin/env python

import string
from random import choice
from re import findall

DEFAULT_LENGTH = 16


class CharPassword(object):
    """
    Generate password consisting of characters
    """
    def __init__(self, length=DEFAULT_LENGTH):
        self.length = self.__check_length(length)
        self.options = ['digits', 'lowercase', 'uppercase', 'punctuation']
        self.table = self.__generate_table()
        self.valid = False
        self.password = self.__generate_password()

    def __generate_password(self):
        while self.valid is False:
            password = ''.join([choice(self.table) for x in range(self.length)])
            self.valid = self.__is_valid(password)
        return password

    def __generate_table(self):
        table = []
        for option in self.options:
            table += getattr(string, option)
        return table

    def __is_valid(self, password):
        mapper = {'digits': '0-9',
                  'lowercase': 'a-z',
                  'uppercase': 'A-Z',
                  'punctuation': string.punctuation}
        for option in self.options:
            if not findall('[%s]' % mapper[option], password):
                self.valid = False
        self.valid = True

    def __check_length(self, length):
        try:
            length = int(length)
        except ValueError:
            length = DEFAULT_LENGTH
        finally:
            return length if length > 0 else DEFAULT_LENGTH
