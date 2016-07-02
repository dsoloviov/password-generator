#!/usr/bin/env python

from random import randint as r


class BasicPassword(object):
    def __init__(self, number, length, options=False):
        self.number = number
        self.length = length
        self.options = options
        self.table = self.__generate_table()

    def get_password(self):
        if self.number > 1:
            return [self.__generate_password() for x in range(self.number)]
        return self.__generate_password()

    def __generate_table(self):
        """
        Generate char table

        Full table:
        table = zip([i for i in range(33, 126)], [chr(k) for k in range(33, 126)])

        digits: 48 - 57
        lower-case letters: 97 - 122
        upper-case letters: 65 - 90
        special symbols: 33 - 47, 58 - 64, 91 - 96, 123 - 125

        chr(97) == 'a'
        """
        table = []
        if self.options:
            if self.options['digits']:
                table += [chr(x) for x in range(48, 58)]
            if self.options['lower']:
                table += [chr(x) for x in range(97, 123)]
            if self.options['upper']:
                table += [chr(x) for x in range(65, 91)]
            if self.options['special']:
                table += [chr(x) for x in range(33, 48)]
                table += [chr(x) for x in range(58, 65)]
                table += [chr(x) for x in range(91, 97)]
                table += [chr(x) for x in range(123, 126)]
        else:
            return dict(enumerate([chr(x) for x in range(33, 126)]))
        return dict(enumerate(table))


    def __generate_password(self):
        return ''.join([self.table[r(0, len(self.table) - 1)] for x in range(self.length)])

if __name__ == '__main__':
    p = BasicPassword(1, 10)
    assert len(p.get_password()) == 10
