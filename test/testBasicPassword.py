#!/usr/bin/env python

import unittest
from src.basicPassword import BasicPassword


class testBasicPassword(unittest.TestCase):
    def test_number_of_passwords(self):
        p = BasicPassword(5, 10)
        self.assertEqual(len(p.get_password()), 5)

    def test_number_of_passwords_zero(self):
        p = BasicPassword(0, 10)
        self.assertEqual(len(p.get_password()), 0)

    def test_length_of_passwords(self):
        p = BasicPassword(1, 10)
        self.assertEqual(len(p.get_password()[0]), 10)

    def test_length_of_passwords_zero(self):
        p = BasicPassword(1, 0)
        self.assertEqual(len(p.get_password()[0]), 0)

    def test_no_options(self):
        p = BasicPassword(1, 10)
        self.assertEqual(len(p.get_password()), 1)
        self.assertEqual(len(p.get_password()[0]), 10)

    def test_complete_options(self):
        p = BasicPassword(1, 10, ['digits', 'lowercase',
                                  'uppercase', 'punctuation'])
        self.assertEqual(len(p.get_password()), 1)
        self.assertEqual(len(p.get_password()[0]), 10)

    def test_incomplete_options(self):
        p = BasicPassword(1, 10, ['digits', 'lowercase'])
        self.assertEqual(len(p.get_password()), 1)
        self.assertEqual(len(p.get_password()[0]), 10)

    def test_options_invalid_parameter(self):
        p = BasicPassword(1, 10, ['digits', 'invalid'])
        self.assertEqual(len(p.get_password()), 1)
        self.assertEqual(len(p.get_password()[0]), 10)
