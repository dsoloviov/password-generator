#!/usr/bin/env python

import unittest
from re import findall
from pgen import getpsw
from string import punctuation
from src.worker import isValid
from src.worker import checkLength
from src.worker import checkOptions


class testGeneratePassword(unittest.TestCase):
    def setUp(self):
        self.options = ['digits', 'lowercase',
                        'uppercase', 'punctuation']
        self.options_invalid = ['digits', 'invalid']

    def assertComplete(self, password):
        self.assertTrue(bool(findall('[0-9]', password)))
        self.assertTrue(bool(findall('[a-z]', password)))
        self.assertTrue(bool(findall('[A-Z]', password)))
        self.assertTrue(bool(findall('[%s]' % punctuation, password)))

    def test_length_of_password(self):
        password = getpsw(10)
        self.assertEqual(len(password), 10)
        self.assertComplete(password)

    def test_length_of_password_zero(self):
        password = getpsw(0)
        self.assertEqual(len(password), 10)
        self.assertComplete(password)

    def test_complete_options(self):
        password = getpsw(10, self.options)
        self.assertEqual(len(password), 10)
        self.assertComplete(password)

    def test_incomplete_options(self):
        password = getpsw(10, self.options[:2])
        self.assertEqual(len(password), 10)
        self.assertTrue(bool(findall('[0-9]', password)))
        self.assertTrue(bool(findall('[a-z]', password)))

    def test_invalid_option(self):
        password = getpsw(10, self.options_invalid)
        self.assertEqual(len(password), 10)
        self.assertTrue(bool(findall('[0-9]', password)))


class testPasswordValidator(unittest.TestCase):
    def setUp(self):
        self.options = ['digits', 'lowercase',
                        'uppercase', 'punctuation']

    def test_validate_wrong(self):
        """
        Here was a bug: True returned on first
        run of validator. Therefore absence of
        uppercase did not fail test
        """
        result = isValid('u?5\'.atu?h', self.options)
        self.assertFalse(bool(result))

    def test_validate_all(self):
        result = isValid('tEs!123', self.options)
        self.assertTrue(bool(result))

    def test_validate_digits_and_lowercase(self):
        result = isValid('test123', self.options[:2])
        self.assertTrue(bool(result))

    def test_validate_no_digits_and_lowercase(self):
        result = isValid('TEST!@#', self.options[:2])
        self.assertFalse(bool(result))

    def test_validate_digits(self):
        result = isValid('test123', [self.options[0]])
        self.assertTrue(bool(result))

    def test_validate_no_digits(self):
        result = isValid('test', [self.options[0]])
        self.assertFalse(bool(result))

    def test_validate_lowercase(self):
        result = isValid('TeST123', [self.options[1]])
        self.assertTrue(bool(result))

    def test_validate_no_lowercase(self):
        result = isValid('TEST123', [self.options[1]])
        self.assertFalse(bool(result))

    def test_validate_uppercase(self):
        result = isValid('tEst123', [self.options[2]])
        self.assertTrue(bool(result))

    def test_validate_no_uppercase(self):
        result = isValid('test123', [self.options[2]])
        self.assertFalse(bool(result))

    def test_validate_special(self):
        result = isValid('t@st123', [self.options[3]])
        self.assertTrue(bool(result))

    def test_validate_no_special(self):
        result = isValid('test123', [self.options[3]])
        self.assertFalse(bool(result))


class testGenerateTable(unittest.TestCase):
    pass


class testCheckLength(unittest.TestCase):
    def test_correct_length(self):
        self.assertEqual(checkLength(13), 13)

    def test_zero_length(self):
        self.assertEqual(checkLength(0), 10)

    def test_negative_length(self):
        self.assertEqual(checkLength(-13), 10)

    def test_invalid_length(self):
        self.assertEqual(checkLength('t'), 10)



class testCheckOptions(unittest.TestCase):
    def setUp(self):
        self.correct_options = ['digits', 'lowercase',
                                'uppercase', 'punctuation']
        self.invalid_options = ['digits', 'lowercase',
                                'invalid', 'punctuation']
        self.all_invalid = ['invalid1', 'invalid2',
                            'invalid3', 'invalid4']

    def test_correct_option(self):
        result = checkOptions(self.correct_options)
        self.assertEqual(len(result), 4)

    def test_invalid_option(self):
        result = checkOptions(self.invalid_options)
        self.assertEqual(len(result), 3)

    def test_all_invalid(self):
        result = checkOptions(self.all_invalid)
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
