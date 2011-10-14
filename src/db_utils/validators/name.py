#!/usr/bin/python
#! -*- coding: utf-8 -*-


""" Validators of Lithuanian names and surnames.
"""


import re

from db_utils.validators.exceptions import ValidationError
from db_utils.decorators.unicode import UnicodeArguments

try:
    from django.utils.translation import ugettext as _
except ImportError:
    _ = lambda text: text


ALPHABET_LT = (
    u'a', u'ą', u'b', u'c', u'č', u'd', u'e', u'ę', u'ė', u'f', u'g',
    u'h', u'i', u'į', u'y', u'j', u'k', u'l', u'm', u'n', u'o', u'p',
    u'r', u's', u'š', u't', u'u', u'ų', u'ū', u'v', u'z', u'ž')


class NameValidator(object):
    """ Validator for name.
    """

    def __init__(
            self, alphabet, validation_exception_type=ValidationError,
            convert=True):
        """

        +   ``alphabet`` -- alphabet, from which name have to be formed.
        +   ``validation_exception_type`` -- what type of exception to
            throw, when validation fails.
        +   ``convert`` -- if True tries to fix name, if False just checks
            if it is correct.

        """

        self.alphabet = alphabet
        self.validation_exception_type = validation_exception_type
        self.convert = convert

    @UnicodeArguments(skip=['self', 0])
    def __call__(self, value):
        """ Checks if given value is correct name.
        """

        if not value:
            raise self.validation_exception_type(_(
                    u'Empty string cannot be a name.'))

        for symbol in value.lower():
            if symbol not in self.alphabet:
                raise self.validation_exception_type(_(
                    u'Symbol "{0}" is not allowed in name.').format(
                            symbol))

        if not self.convert and not value.istitle():
            raise self.validation_exception_type(_(u'Wrong name format.'))
        else:
            return value.title()


class NamesValidator(object):
    """ Validator for names (first and middle).
    """

    def __init__(
            self, alphabet, validation_exception_type=ValidationError,
            convert=True):
        """

        +   ``alphabet`` -- alphabet, from which name have to be formed.
        +   ``validation_exception_type`` -- what type of exception to
            throw, when validation fails.
        +   ``convert`` -- if True tries to fix name, if False just checks
            if it is correct.

        """

        self.validation_exception_type = validation_exception_type
        self.name_validator = NameValidator(
                alphabet, validation_exception_type, convert)
        self.convert = convert

    @UnicodeArguments(skip=['self', 0])
    def __call__(self, value):
        """ Checks if given value is a name(s), separated by whitespace.
        """

        values = value.strip().split()
        if not (1 <= len(values) <= 2):
            raise self.validation_exception_type(_(
                u'One or two names are allowed.'))

        names = []
        for word in values:
            names.append(self.name_validator(word))

        name = u' '.join(names)
        if not self.convert:
            if name != value:
                raise self.validation_exception_type(_(
                        u'Names can\'t have surounding whitespace.'))

        return name


class SurnameValidator(NamesValidator):
    """ Validator for surname.
    """

    @UnicodeArguments(skip=['self', 0])
    def __call__(self, value):
        """ Checks if given value is a surname.

        Surname can be two words separated by whitespace or hyphen.
        """

        if u'-' in value or u'\u2010' in value:
            hyphen = True
            value = value.replace(u'-', u' ').replace(u'\u2010', u' ')
        else:
            hyphen = False

        values = value.strip().split()
        if not (1 <= len(values) <= 2):
            raise self.validation_exception_type(_(
                u'Just one or two words in surname are allowed.'))

        names = []
        for value in values:
            names.append(self.name_validator(value))

        if hyphen:
            return u'\u2010'.join(names)
        else:
            return u' '.join(names)


class FullName(object):
    """ Representation of full name.
    """

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __unicode__(self):
        return u'{0.name} {0.surname}'.format(self)


class FullNameValidator(object):
    """ Validator for full Lithuanian name.

    Last word or pair of words joined by hyphen is assumed to be a
    surname. Everything before are assumed to be a name.

    """

    def __init__(
            self, alphabet, validation_exception_type=ValidationError,
            convert=True):
        """

        +   ``alphabet`` -- alphabet, from which name have to be formed.
        +   ``validation_exception_type`` -- what type of exception to
            throw, when validation fails.
        +   ``convert`` -- if True tries to fix name, if False just checks
            if it is correct.

        """

        self.names_validator = NamesValidator(
                alphabet, validation_exception_type, convert)
        self.surname_validator = SurnameValidator(
                alphabet, validation_exception_type, convert)
        self.validation_exception_type = validation_exception_type

    @UnicodeArguments(skip=['self', 0])
    def __call__(self, value):
        """ Checks if given value is a name(s), separated by whitespace.
        """

        value = re.sub(u'\s*-\s*', u'-', value)
        value = re.sub(u'\s*\u2010\s*', u'\u2010', value)
        values = value.strip().split()
        return FullName(
                self.names_validator(u' '.join(values[:-1])),
                self.surname_validator(values[-1]))
