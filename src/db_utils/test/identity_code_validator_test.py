#!/usr/bin/python


""" Tests for db_utils.validators.identity_code.
"""


import unittest
from db_utils.validators.exceptions import ValidationError
from db_utils.validators.identity_code import IdentityCodeValidator


class CustomValidationError(Exception):
    """ Custom validation error.
    """


class IdentityCodeValidatorTest(unittest.TestCase):
    """ Tests for ``IdentityCodeValidator``.
    """

    def test_custom_exception(self):

        validator = IdentityCodeValidator(
                validation_exception_type=CustomValidationError)
        #self.assertRaises(CustomValidationError, validator, u'foo')

    def test_correct_codes(self):

        validator = IdentityCodeValidator()

        code = validator(u'19901010003')
        assert unicode(code) == u'19901010003'
        assert code.gender == u'm'
        assert code.get_birth_date() == u'1899-01-01'

        code = validator(u'29901010004')
        assert unicode(code) == u'29901010004'
        assert code.gender == u'f'
        assert code.get_birth_date() == u'1899-01-01'

        code = validator(u'39901010005')
        assert unicode(code) == u'39901010005'
        assert code.gender == u'm'
        assert code.get_birth_date() == u'1999-01-01'

        code = validator(u'49901010006')
        assert unicode(code) == u'49901010006'
        assert code.gender == u'f'
        assert code.get_birth_date() == u'1999-01-01'

        code = validator(u'59901010007')
        assert unicode(code) == u'59901010007'
        assert code.gender == u'm'
        assert code.get_birth_date() == u'2099-01-01'

        code = validator(u'69901010008')
        assert unicode(code) == u'69901010008'
        assert code.gender == u'f'
        assert code.get_birth_date() == u'2099-01-01'

        code = validator(u'60902021008')
        assert unicode(code) == u'60902021008'
        assert code.gender == u'f'
        assert code.get_birth_date() == u'2009-02-02'

        code = validator(u'60902021008')
        assert unicode(code) == u'60902021008'
        assert code.gender == u'f'
        assert code.get_birth_date() == u'2009-02-02'

        self.assertRaises(ValidationError, validator, u'01234067890')

    def test_incorrect_codes(self):

        validator = IdentityCodeValidator()

        self.assertRaises(ValidationError, validator, u'foo')
        self.assertRaises(ValidationError, validator, u'1234567890')
        self.assertRaises(ValidationError, validator, u'609020210084')
        self.assertRaises(ValidationError, validator, u'12345678901')
        self.assertRaises(ValidationError, validator, u'00902021004')
        self.assertRaises(ValidationError, validator, u'61102291005')
