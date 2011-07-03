#!/usr/bin/python

""" Tests for db_utils.validators.phone_number.
"""


import unittest


from db_utils.validators.exceptions import ValidationError
from db_utils.validators.phone_number import simple_validator


class SimpleValidator(unittest.TestCase):
    """ Tests for simple validator.
    """

    def test_correct_value(self):

        self.assertEqual(simple_validator('3'), 3)

    def test_incorrect_value(self):

        self.assertRaises(ValidationError, simple_validator, 'a')

