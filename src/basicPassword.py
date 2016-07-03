#!/usr/bin/env python

from random import randint as simple_rand
import string


class BasicPassword(object):
    def __init__(self, number, length, options=False):
        self.number = number
        self.length = length
        self.options = options
        self.table = self.generate_table()

    def get_password(self):
        return [self.generate_password() for x in range(self.number)]

    def generate_table(self):
        table = []
        if self.options:
            for option in self.options:
                try:
                    table += getattr(string, option)
                except AttributeError:
                    pass
        else:
            return dict(enumerate(string.digits +
                                  string.lowercase +
                                  string.uppercase +
                                  string.punctuation))
        return dict(enumerate(table))

    def generate_password(self):
        return ''.join([self.table[self.random()] for x in range(self.length)])

    def random(self):
        return simple_rand(0, len(self.table) - 1)


if __name__ == '__main__':
    p = BasicPassword(1, 10)
    assert len(p.get_password()) == 10
