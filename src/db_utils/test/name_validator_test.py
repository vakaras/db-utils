#!/usr/bin/python

""" Tests for db_utils.validators.name.
"""


import unittest


from db_utils.validators.exceptions import ValidationError
from db_utils.validators.name import (
        ALPHABET_LT, NameValidator, NamesValidator, SurnameValidator,
        FullNameValidator,
        )


class CustomValidationError(Exception):
    """ Custom validation error.
    """


class NameValidatorTest(unittest.TestCase):
    """ Tests for ``NameValidator``.
    """

    def test_custom_exception(self):

        validator = NameValidator(
                ALPHABET_LT,
                validation_exception_type=CustomValidationError,
                convert=False)
        self.assertRaises(CustomValidationError, validator, u'foo')

    def test_correct_names(self):

        validator = NameValidator(ALPHABET_LT)
        assert validator(u'Foo') == u'Foo'
        assert validator(u'fOo') == u'Foo'

    def test_incorrect_names(self):

        validator = NameValidator(ALPHABET_LT)
        self.assertRaises(ValidationError, validator, u'')
        self.assertRaises(ValidationError, validator, u' Foo')

        validator = NameValidator(ALPHABET_LT, convert=False)
        self.assertRaises(ValidationError, validator, u'fOo')


class NamesValidatorTest(unittest.TestCase):
    """ Tests for ``NamesValidator``.
    """

    def test_custom_exception(self):

        validator = NamesValidator(
                ALPHABET_LT,
                validation_exception_type=CustomValidationError,
                convert=False)
        self.assertRaises(CustomValidationError, validator, u'foo')

    def test_correct_names(self):

        validator = NamesValidator(ALPHABET_LT)

        assert validator(u'  Foo   ') == u'Foo'
        assert validator(u' Foo  ') == u'Foo'
        assert validator(u'  Foo Bar  ') == u'Foo Bar'
        assert validator(u' fOo  bAr') == u'Foo Bar'

    def test_incorrect_names_without_convert(self):

        validator = NamesValidator(ALPHABET_LT, convert=False)

        self.assertRaises(ValidationError, validator, u'  Foo   ')
        self.assertRaises(ValidationError, validator, u' Foo  ')
        self.assertRaises(ValidationError, validator, u'  Foo Bar  ')
        self.assertRaises(ValidationError, validator, u' fOo  bAr')

    def test_incorrect_names_with_convert(self):

        validator = NamesValidator(ALPHABET_LT)

        self.assertRaises(ValidationError, validator, u'Xar')
        self.assertRaises(ValidationError, validator, u'foo bar foobarer')


class SurnameValidatorTest(unittest.TestCase):
    """ Tests for ``SurnameValidator``.
    """

    def test_correct_names(self):

        validator = SurnameValidator(ALPHABET_LT)

        assert validator(u'  Foo   ') == u'Foo'
        assert validator(u' Foo  ') == u'Foo'
        assert validator(u'  Foo Bar  ') == u'Foo Bar'
        assert validator(u' fOo  bAr') == u'Foo Bar'

        assert validator(u' Foo - bar  ') == u'Foo\u2010Bar'
        assert validator(u' fOo \u2010    Bar  ') == u'Foo\u2010Bar'
        assert validator(u' Foo - -- - - -bar  ') == u'Foo\u2010Bar'

    def test_incorrect_names(self):

        validator = SurnameValidator(ALPHABET_LT)

        self.assertRaises(ValidationError, validator, u'Xar')
        self.assertRaises(ValidationError, validator, u'foo bar foobarer')
        self.assertRaises(ValidationError, validator, u'foo-bar-foobarer')


class FullNameValidatorTest(unittest.TestCase):
    """ Tests for ``FullNameValidator``.
    """

    def test_custom_exception(self):

        validator = FullNameValidator(
                ALPHABET_LT,
                validation_exception_type=CustomValidationError,
                convert=False)
        self.assertRaises(CustomValidationError, validator, u'Foo')

    def test_correct_names(self):

        validator = FullNameValidator(ALPHABET_LT)

        name = validator(u'  Foo  bar ')
        assert name.name == u'Foo'
        assert name.surname == u'Bar'
        assert unicode(name) == u'Foo Bar'

        name = validator(u'  Foo  bar  bar ')
        assert name.name == u'Foo Bar'
        assert name.surname == u'Bar'
        assert unicode(name) == u'Foo Bar Bar'

        name = validator(u'  Foo  bar - bar ')
        assert name.name == u'Foo'
        assert name.surname == u'Bar\u2010Bar'
        assert unicode(name) == u'Foo Bar\u2010Bar'

        name = validator(u' fOO  Foo  bar - bar ')
        assert name.name == u'Foo Foo'
        assert name.surname == u'Bar\u2010Bar'
        assert unicode(name) == u'Foo Foo Bar\u2010Bar'

    def test_incorrect_names(self):

        validator = FullNameValidator(ALPHABET_LT)

        self.assertRaises(ValidationError, validator, u'Foo')
        self.assertRaises(ValidationError, validator, u'foo -bar-foobarer')
        self.assertRaises(ValidationError, validator, u' Foo - bar  ')
        self.assertRaises(ValidationError, validator, u' fOo \u2010  Bar ')
