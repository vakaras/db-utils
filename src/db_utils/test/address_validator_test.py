#!/usr/bin/python
# -*- coding: utf-8 -*-


""" Tests for db_utils.validators.phone_number.
"""


import unittest


from db_utils.validators.exceptions import ValidationError
from db_utils.validators.address import LTAddressValidator
from db_utils.validators.address import AddressValidator


class LTAddressValidatorTest(unittest.TestCase):
    """ Tests for ``LTAddressValidatorTest``.
    """

    def test_correct_addresses(self):

        validator = LTAddressValidator()

        address = validator(u'A.   B. C.   Dudausko  g. 4, 12345 Vilnius')
        assert unicode(address) == u'A. B. C. Dudausko g. 4, 12345 Vilnius'
        assert address[u'building'] == None
        assert address[u'town'] == u'Vilnius'
        assert address[u'post_code'] == u'12345'
        assert address[u'street'] == u'A. B. C. Dudausko gatv\u0117'
        assert address[u'flat'] == None
        assert address[u'house'] == u'4'

        address = validator(u'R. D. K. Ba pl. 4/2-1, LT-00000 Kazlų rūda')
        assert address[u'building'] == u'2'
        assert address[u'town'] == u'Kazlų rūda'
        assert address[u'post_code'] == u'00000'
        assert address[u'street'] == u'R. D. K. Ba plentas'
        assert address[u'flat'] == u'1'
        assert address[u'house'] == u'4'

        validator(u'Žemynos g. 41-11, 06131 Vilnius')
        validator(u'Sodų g. 12, 26111 Elektrėnai')
        validator(u'Gedimino pr. 40/1, 01501 Vilnius')

        address = validator(
                u'Plento g. 17, Ariogala, 60249 Raseinių r. sav.')
        assert address[u'building'] == None
        assert address[u'town'] == u'Ariogala'
        assert address[u'post_code'] == u'60249'
        assert address[u'street'] == u'Plento gatvė'
        assert address[u'flat'] == None
        assert address[u'house'] == u'17'
        assert (address[u'local_government'] ==
                u'Raseinių rajono savivaldybė')

        validator(u'Saulės g. 7, Kietaviškės, 21411 Elektrėnų sav.')
        address = validator(
                u'Spalviškių k., Kirdonių pšt., 41377 Biržų r. sav.')
        assert address[u'local_government'] == u'Biržų rajono savivaldybė'
        assert address[u'post'] == u'Kirdonių paštas'
        assert address[u'post_code'] == u'41377'
        assert address[u'village'] == u'Spalviškių kaimas'


        # Tarptautinis:
        #validator(u'Subačiaus g. 120, LT-11345 Vilnius, LITHUANIA')

    def test_incorrect_addresses(self):

        validator = LTAddressValidator()

        self.assertRaises(
                ValidationError, validator,
                u'Žemynos g-vė 41-11, 06131 Vilnius')


class AddressValidatorTest(unittest.TestCase):
    """ Tests for ``AddressValidatorTest``.
    """

    def test_correct_addresses(self):

        validator = AddressValidator(u'LITHUANIA')

        address = validator(u'A.   B. C.   Dudausko  g. 4, 12345 Vilnius')
        assert unicode(address) == u'A. B. C. Dudausko g. 4, 12345 Vilnius'
        assert address[u'building'] == None
        assert address[u'country'] == u'LITHUANIA'
        assert address[u'town'] == u'Vilnius'
        assert address[u'post_code'] == u'12345'
        assert address[u'street'] == u'A. B. C. Dudausko gatv\u0117'
        assert address[u'flat'] == None
        assert address[u'house'] == u'4'

        address = validator(u'R. D. K. Ba pl. 4/2-1, LT-00000 Kazlų rūda')
        assert address[u'building'] == u'2'
        assert address[u'country'] == u'LITHUANIA'
        assert address[u'town'] == u'Kazlų rūda'
        assert address[u'post_code'] == u'00000'
        assert address[u'street'] == u'R. D. K. Ba plentas'
        assert address[u'flat'] == u'1'
        assert address[u'house'] == u'4'

        validator(u'Žemynos g. 41-11, 06131 Vilnius')
        validator(u'Sodų g. 12, 26111 Elektrėnai')
        validator(u'Gedimino pr. 40/1, 01501 Vilnius')

        address = validator(
                u'Plento g. 17, Ariogala, 60249 Raseinių r. sav.')
        assert address[u'building'] == None
        assert address[u'country'] == u'LITHUANIA'
        assert address[u'town'] == u'Ariogala'
        assert address[u'post_code'] == u'60249'
        assert address[u'street'] == u'Plento gatvė'
        assert address[u'flat'] == None
        assert address[u'house'] == u'17'
        assert (address[u'local_government'] ==
                u'Raseinių rajono savivaldybė')

        validator(u'Saulės g. 7, Kietaviškės, 21411 Elektrėnų sav.')
        address = validator(
                u'Spalviškių k., Kirdonių pšt., 41377 Biržų r. sav.')
        assert address[u'country'] == u'LITHUANIA'
        assert address[u'local_government'] == u'Biržų rajono savivaldybė'
        assert address[u'post'] == u'Kirdonių paštas'
        assert address[u'post_code'] == u'41377'
        assert address[u'village'] == u'Spalviškių kaimas'

        address = validator(
                u'Subačiaus g. 120, LT-11345 Vilnius, LITHUANIA')
        assert address[u'country'] == u'LITHUANIA'

    def test_incorrect_addresses(self):

        validator = AddressValidator(u'LITHUANIA')

        self.assertRaises(
                ValidationError, validator,
                u'Žemynos g-vė 41-11, 06131 Vilnius')
        self.assertRaises(
                ValidationError, validator,
                u'Subačiaus g. 120, LT-11345 Vilnius, Lithuania')
        self.assertRaises(
                ValidationError, validator,
                u'Subačiaus g. 120, LT-11345 Vilnius, LATVIA')
