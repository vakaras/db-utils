#!/usr/bin/python


""" Lists all validators.
"""


from db_utils.validators.phone_number import simple_validator
from db_utils.validators.name import (
        NameValidator, NamesValidator,
        SurnameValidator, FullNameValidator)
