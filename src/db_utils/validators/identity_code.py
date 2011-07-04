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
            g, y1, y2, m1, m2, d1, d2, x1, x2, x3, k = [
                int(i) for i in value]
        except ValueError:
            raise self.validation_exception_type(
                    u'Identity code should have 11 digits.')

        sum1 = (g*1+y1*2+y2*3+m1*4+m2*5+d1*6+d2*7+x1*8+x2*9+x3*1)%11
        sum2 = (g*3+y1*4+y2*5+m1*6+m2*7+d1*8+d2*9+x1*1+x2*2+x3*3)%11
        sum3 = 0

        if sum1 != 10:
            case = [sum1, 1]
        elif sum2 != 10:
            case = [sum2, 2]
        else:
            case = [sum3, 3]

        if k != case[0]:
            raise self.validation_exception_type((
                    u'Incorrect identity code. Control digit is {0} and '
                    u'by case {2} was counted {1}.').format(
                        k, case[0], case[1]))

        if g in (1, 3, 5):
            gender = u'm'
        elif g in (2, 4, 6):
            gender = u'f'
        else:
            raise self.validation_exception_type(
                    u'Unknown gender: {0}.'.format(g))

        if g in (1, 2):
            year = u'18'
        elif g in (3, 4):
            year = u'19'
        else:
            year = u'20'
        try:
            birth_date = datetime.date(
                int(u'{0}{1}{2}'.format(year, y1, y2)),
                int(u'{0}{1}'.format(m1, m2)),
                int(u'{0}{1}'.format(d1, d2)))
        except ValueError:
            raise self.validation_exception_type(
                    u'Wrong birth date.'.format(g))

        return IdentityCode(value, gender, birth_date)
