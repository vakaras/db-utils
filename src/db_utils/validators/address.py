#!/usr/bin/python
# -*- coding: utf-8 -*-


""" Validators of addresses.
"""


import re

from db_utils.validators.exceptions import ValidationError
from db_utils.decorators.unicode import UnicodeArguments


class Address(dict):
    """ Address with metadata associated with it.
    """

    def __init__(self, address):
        super(Address, self).__init__()
        self.address = address

    def __unicode__(self):
        return self.address


class LTAddressValidator(object):
    """ Validates if given string represents valid Lithuania address.

    Recommendations for writing addresses can be found
    `here <http://www.post.lt/lt/?id=1218>`_.

    """

    def __init__(self,
            validation_exception_type=ValidationError,
            convert=True):
        """
        +   ``validation_exception_type`` -- what type of exception to
            throw, when validation fails.
        +   ``convert`` -- if True tries to convert phone number to
            international form, if False just checks if phone number
            is in international form.
        """

        self.validation_exception_type = validation_exception_type
        self.convert = convert

    @UnicodeArguments(skip=['self', 0])
    def __call__(self, value):
        """ Checks if given value is correct address.
        """

        location_types = {
            u'kaimas': [u'k.',],
            #u'korpusas': [u'K',],
            #u'miestas': [u'm.',],
            u'miesto': [u'm.',],        # Warning: Possibly a bug.
            u'miestelis': [u'mstl.',],
            u'paštas': [u'pšt.',],
            #u'rajonas': [u'r.',],
            u'rajono': [u'r.',],        # Warning: Possibly a bug.
            u'savivaldybė': [u'sav.',],
            }

        street_types = {
            u'aikštė': [u'a.',],
            u'alėja': [u'al.',],
            u'gatvė': [u'g.',],
            u'kelias': [u'kel.',],
            u'plentas': [u'pl.',],
            u'prospektas': [u'pr.',],
            u'skersgatvis': [u'skg.',],
            u'skveras': [u'skv.',],
            u'takas': [u'tak.',],
            }

        # Normalize whitespace.
        whitespace = re.compile(ur'\s+', re.UNICODE)
        value = whitespace.sub(u' ', value)

        # Expand.
        for street_type, replacements in street_types.items():
            for replacement in replacements:
                value = value.replace(replacement, street_type)
        for location_type, replacements in location_types.items():
            for replacement in replacements:
                value = value.replace(replacement, location_type)

        parts_list = [
            (u'l', ur'[a-ząčęėįšųūž]'),
            (u'L', ur'[A-ZĄČĘĖĮŠŲŪŽ]'),
            (u'street_type', ur'({0})'.format(
                u'|'.join(street_types.keys()))),

            (u'street', ur'(?P<street>({L}\. )*({L}{l}+ )+{street_type})'),
            (u'house', ur'(?P<house>\d+)'),
            (u'building', ur'(/(?P<building>\d+))?'),
            (u'flat', ur'(-(?P<flat>\d+))?'),
            (u'post_code', ur'(LT-)?(?P<post_code>\d{{5}})'),
            (u'town', ur'(?P<town>{L}{l}+( {L}?{l}+)*)'),
            (u'local_government',
                ur'(?P<local_government>{L}{l}+( {L}{l}+)? '
                ur'(rajon(o|as) |miest(o|as) )?savivaldybė)'),
            (u'village', ur'(?P<village>{L}{l}+( {L}?{l}+)* kaimas)'),
            (u'post', ur'(?P<post>{L}{l}+( {L}?{l}+)* paštas)'),
            ]

        correct_address_patterns = [
            (ur'^{street} {house}{building}{flat}, {post_code} {town}$'),
            (ur'^{street} {house}{building}{flat}, {town}, {post_code} '
                ur'{local_government}$'),
            (ur'^{village}, {post}, {post_code} {local_government}$'),
            ]

        parts = {}
        for key, val in parts_list:
            parts[key] = val.format(**parts)

        for address_pattern in correct_address_patterns:
            address_pattern = address_pattern.format(**parts)
            match = re.match(address_pattern, value, re.UNICODE)
            if match:
                for street_type, replacements in street_types.items():
                    rexp = re.compile(
                            ur'(^|\s*){0}(\s*|$)'.format(street_type),
                            re.UNICODE)
                    value = rexp.sub(
                            ur'\1{0}\2'.format(replacements[0]), value)
                for location_type, replacements in location_types.items():
                    rexp = re.compile(
                            ur'(^|\s*){0}(\s*|$)'.format(location_type),
                            re.UNICODE)
                    value = rexp.sub(
                            ur'\1{0}\2'.format(replacements[0]), value)
                address = Address(value)
                address.update(match.groupdict())
                return address
        raise self.validation_exception_type(u'Incorrect address.')


class AddressValidator(object):
    """ Validates if given string represents valid address.
    """

    def __init__(self, default_country,
            validation_exception_type=ValidationError,
            convert=True):
        """
        +   ``default_country`` -- if country is not defined in address it
            is assumed that country is this.
        +   ``validation_exception_type`` -- what type of exception to
            throw, when validation fails.
        +   ``convert`` -- if True tries to convert phone number to
            international form, if False just checks if phone number
            is in international form.
        """

        self.default_country = default_country
        self.validation_exception_type = validation_exception_type
        self.convert = convert
        self.lt_validator = LTAddressValidator(
                validation_exception_type, convert)

    @UnicodeArguments(skip=['self', 0])
    def __call__(self, value):
        """ Checks if given value is correct address.
        """

        match = re.match(
                ur'^(?P<address>.*), (?P<country>[A-Z]+)$', value,
                re.UNICODE)
        if match:
            group_dict = match.groupdict()
            country = group_dict[u'country']
            value = group_dict[u'address']
        else:
            country = self.default_country

        if country != u'LITHUANIA':
            # Not implemented.
            raise self.validation_exception_type(
                    u'Unknown country {0}.'.format(country))
        else:
            address = self.lt_validator(value)
            address[u'country'] = country
            return address
