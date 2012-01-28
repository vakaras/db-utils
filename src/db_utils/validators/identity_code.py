#!/usr/bin/python


""" Validator of Lithuanian identity code.
"""


import datetime

from db_utils.validators.exceptions import ValidationError
from db_utils.decorators.unicode import UnicodeArguments


class IdentityCode(object):
    """ Identity code with metadata associated with it.
    """

    def __init__(self, code, gender, birth_date):
        self.code = code
        self.gender = gender
        self.birth_date = birth_date

    def get_birth_date(self):
        """ Returns birth date as Unicode string.
        """

        return u'{0.year:4}-{0.month:02}-{0.day:02}'.format(self.birth_date)

    def __unicode__(self):
        return self.code


class IdentityCodeValidator(object):
    """ Validates if given string represents correct identity code.
    """

    def __init__(self, validation_exception_type=ValidationError):
        """

        +   ``validation_exception_type`` -- what type of exception to
            throw, when validation fails.

        """

        self.validation_exception_type = validation_exception_type

    @UnicodeArguments(skip=['self', 0])
    def __call__(self, value):
        """ Checks if given value is correct identity code.
        """

        try:
            digits = [int(i) for i in value]
        except ValueError:
            raise self.validation_exception_type(
                    u'Identity code should have only digits.')
        if len(digits) != 11:
            raise self.validation_exception_type(
                    u'Identity code should have exactly 11 digits.')
        gender_digit = digits[0]
        control_digit = digits[-1]

        case = None
        for case, multipliers in enumerate([
            range(1, 10) + [1], range(3, 10) + range(1, 4)]):
            counted_control_digit = sum([
                digit * multiplier
                for digit, multiplier in zip(digits, multipliers)]) % 11
            if counted_control_digit != 10:
                case -= 1
                break
        if counted_control_digit == 10:
            counted_control_digit = 0
        case += 1

        if control_digit != counted_control_digit:
            raise self.validation_exception_type((
                    u'Incorrect identity code. Control digit is {0} and '
                    u'by case {2} was counted {1}.').format(
                        control_digit, counted_control_digit, case+1))

        if gender_digit in (1, 3, 5):
            gender = u'm'
        elif gender_digit in (2, 4, 6):
            gender = u'f'
        else:
            raise self.validation_exception_type(
                    u'Unknown gender: {0}.'.format(gender_digit))

        if gender_digit in (1, 2):
            year = u'18'
        elif gender_digit in (3, 4):
            year = u'19'
        else:
            year = u'20'
        try:
            birth_date = datetime.date(
                int(u'{0}{1}{2}'.format(year, digits[1], digits[2])),
                int(u'{0}{1}'.format(digits[3], digits[4])),
                int(u'{0}{1}'.format(digits[5], digits[6])))
        except ValueError:
            raise self.validation_exception_type(u'Wrong birth date.')

        return IdentityCode(value, gender, birth_date)
