#!/usr/bin/python


""" Validators of phone numbers.
"""


from db_utils.validators.exceptions import ValidationError


def simple_validator(value):
    """ Checks if value is an number.
    """

    try:
        return int(value)
    except ValueError:
        raise ValidationError(u'Not a number: {0}'.format(value))
