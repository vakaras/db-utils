#!/usr/bin/python


""" Tests for db_utils.validators.phone_number.
"""


import unittest


from db_utils.validators.exceptions import ValidationError
from db_utils.validators.phone_number import simple_validator
from db_utils.validators.phone_number import PhoneNumberValidator


class SimpleValidator(unittest.TestCase):
    """ Tests for simple validator.
    """

    def test_correct_value(self):

        self.assertEqual(simple_validator('3'), 3)

    def test_incorrect_value(self):

        self.assertRaises(ValidationError, simple_validator, 'a')


class CustomValidationError(Exception):
    """ Custom validation error.
    """


class PhoneNumberValidatorTest(unittest.TestCase):
    """ Tests for ``PhoneNumberValidator``.
    """

    def test_custom_exception(self):

        validator = PhoneNumberValidator(
                default_country_code=u'370',
                validation_exception_type=CustomValidationError,
                convert=False)
        self.assertRaises(CustomValidationError, validator, u'foo')

    def test_correct_numbers(self):

        validator = PhoneNumberValidator(u'370')

        # Mobile phone numbers.
        for input_data in (
                u'0037061234567',
                u'+37061234567',
                u'861234567',
                861234567,
                ):
            number = validator(input_data)
            assert number.number == u'1234567'
            assert number.country == u'Lietuva'
            assert number.country_code == u'370'
            assert number.region is None
            assert number.region_code == u'6'
            assert unicode(number) == u'+37061234567'

        number = validator(u'+37161234567')
        assert number.number == u'1234567'
        assert number.country == u'Latvija'
        assert number.country_code == u'371'
        assert number.region is None
        assert number.region_code == u'6'
        assert unicode(number) == u'+37161234567'

        number = validator(u'+37151234567')
        assert number.number == u'51234567'
        assert number.country == u'Latvija'
        assert number.country_code == u'371'
        assert number.region is None
        assert number.region_code == u''
        assert unicode(number) == u'+37151234567'

        # Non mobile phone numbers.
        for input_data in (
                u'0037051234567',
                u'+37051234567',
                u'851234567'):
            number = validator(input_data)
            assert number.number == u'1234567'
            assert number.country == u'Lietuva'
            assert number.country_code == u'370'
            assert number.region == u'Vilnius'
            assert number.region_code == u'5'
            assert unicode(number) == u'+37051234567'

    def test_incorrect_numbers(self):

        validator = PhoneNumberValidator(u'370')
        self.assertRaises(ValidationError, validator, u'+370')
        self.assertRaises(ValidationError, validator, u'1234567')
        self.assertRaises(ValidationError, validator, u'+37861234567')
        self.assertRaises(ValidationError, validator, u'+37081234567')
        self.assertRaises(ValidationError, validator, u'+370512345678')
        self.assertRaises(ValidationError, validator, u'+3705123456')

        self.assertRaises(ValidationError, validator, None)
        self.assertRaises(ValidationError, validator, u'')
        self.assertRaises(ValidationError, validator, u'aba')

        validator = PhoneNumberValidator(u'370', convert=False)
        self.assertRaises(ValidationError, validator, u'851234567')
