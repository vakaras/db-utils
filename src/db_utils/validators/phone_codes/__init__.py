#!/usr/bin/python


""" Lists of phone number codes.
"""


from db_utils.validators.phone_codes.countries import COUNTRIES_PHONE_CODES


COUNTRIES_PHONE_CODES_BY_CODE = dict([
    (info['code'], info) for info in COUNTRIES_PHONE_CODES])
