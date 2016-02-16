#!/usr/bin/python


""" Validators of phone numbers.
"""


from db_utils.validators.exceptions import ValidationError
from db_utils.validators.phone_codes import COUNTRIES_PHONE_CODES_BY_CODE
from db_utils.validators.phone_codes import COUNTRIES_PHONE_CODES
from db_utils.decorators.unicode import UnicodeArguments


def simple_validator(value):
    """ Checks if value is an number.
    """

    try:
        return int(value)
    except ValueError:
        raise ValidationError(u'Not a number: {0}'.format(value))


class PhoneNumber(object):
    """ Phone number with metadata associated with it.
    """

    @UnicodeArguments(skip=['self', 0])
    def __init__(self, input_data):
        self.input_data = input_data
        self.number = None
        self.country = None
        self.country_code = None
        self.region = None
        self.region_code = None

    def __str__(self):
        return u'+{0.country_code}{0.region_code}{0.number}'.format(self)


class PhoneNumberValidator(object):
    """ Validates if given string represents correct phone number.
    """

    def __init__(
            self, default_country_code,
            validation_exception_type=ValidationError,
            convert=True):
        """

        +   ``default_country_code`` -- if country code is not provided it
            is assumed that country is this.
        +   ``validation_exception_type`` -- what type of exception to
            throw, when validation fails.
        +   ``convert`` -- if True tries to convert phone number to
            international form, if False just checks if phone number
            is in international form.

        """

        self.default_country = COUNTRIES_PHONE_CODES_BY_CODE[
                default_country_code]
        self.validation_exception_type = validation_exception_type
        self.convert = convert

    @UnicodeArguments(skip=['self', 0])
    def __call__(self, value):
        """ Checks if given value is correct phone number.
        """

        number = PhoneNumber(input_data=value)

        # Checks if number is in international form.
        already_international = False
        if value.startswith(u'+'):
            already_international = True
            value = value[1:]
        elif not self.convert:
            raise self.validation_exception_type(
                    u'Phone number is not in international form.')
        if value.startswith(u'00'):
            already_international = True
            value = value[2:]
        if already_international:
            value = self.parse_country_code(value, number)
        elif value.startswith(u'8'):
            value = value[1:]
            number.country_code = self.default_country['code']
            number.country = self.default_country['country']
        else:
            raise self.validation_exception_type(
                    u'Phone number have to be in international form or '
                    u'start with 8.')

        value = self.parse_region_code(value, number)
        number.number = value

        if COUNTRIES_PHONE_CODES_BY_CODE[number.country_code].get(
                'number_length_min', 0) + 1 > len(str(number)):
            raise self.validation_exception_type((
                    u'Phone number in international form should have '
                    u'at least {0} digits.').format(
                        COUNTRIES_PHONE_CODES_BY_CODE[
                            number.country_code].get(
                                'number_length_min', 0)))
        if COUNTRIES_PHONE_CODES_BY_CODE[number.country_code].get(
                'number_length_max', 100) + 1 < len(str(number)):
            raise self.validation_exception_type((
                    u'Phone number in international form should have '
                    u'no more than {0} digits.').format(
                        COUNTRIES_PHONE_CODES_BY_CODE[
                            number.country_code].get(
                                'number_length_max', 0)))

        return number

    def parse_country_code(self, value, number):
        """ Extracts country code form ``value`` and sets it to
        ``number.country_code``. Returns local phone number.
        """

        for country in COUNTRIES_PHONE_CODES:

            if value.startswith(country['code']):
                number.country_code = country['code']
                number.country = country['country']
                return value[len(country['code']):]

        raise self.validation_exception_type(u'Unknown country.')

    def parse_region_code(self, value, number):
        """ Extracts region code from ``value`` and sets it to
        ``number.region_code``. Returns local phone number.
        """

        if value.startswith(u'6'):
            # If mobile phone number.
            number.region_code = u'6'
            number.region = None
            return value[1:]

        if not COUNTRIES_PHONE_CODES_BY_CODE[number.country_code].has_key(
                'regions'):
            number.region_code = u''
            number.region = None
            return value

        if not value:
            raise self.validation_exception_type(
                    u'No region info in phone number found. '
                    u'Maybe number is too short?')

        for region in COUNTRIES_PHONE_CODES_BY_CODE[
                number.country_code]['regions']:

            if value.startswith(region['code']):
                number.region_code = region['code']
                number.region = region['region']
                return value[len(region['code']):]

        raise self.validation_exception_type(
                u'Unknown phone number region.')
