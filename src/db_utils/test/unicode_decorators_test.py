#!/usr/bin/python
# -*- coding: utf-8 -*-


""" Tests for db_utils.decorators.unicode.
"""


import unittest


from db_utils.decorators.unicode import to_unicode, to_bytes
from db_utils.decorators.unicode import UnicodeArguments


class Converters(unittest.TestCase):
    """ Tests for ``to_unicode`` and for ``to_bytes``.
    """

    def assert_equal(self, a, b):
        """ Checks if a == b and type(a) == type(b).
        """

        self.assertEqual(a, b)
        self.assertEqual(type(a), type(b))

    def test_to_unicode(self):

        for data, rez in [
                (4, u'4'),
                ('hello', u'hello'),
                ('a\xc4\x8di\xc5\xab', u'ačiū'),
                ]:
            self.assert_equal(to_unicode(data), rez)

    def test_to_bytes(self):

        for data, rez in [
                (4, '4'),
                (u'hello', 'hello'),
                (u'ačiū', 'a\xc4\x8di\xc5\xab'),
                ]:
            self.assert_equal(to_bytes(data), rez)


class UnicodeArgumentsTest(unittest.TestCase):
    """ Tests for ``UnicodeArguments``.
    """

    def function_test(self):

        @UnicodeArguments()
        def f1(a, b, c):
            return a, b, c

        self.assertEqual(f1(1, 2, 3), (u'1', u'2', u'3'))
        self.assertEqual(f1(1, 2, c=4), (u'1', u'2', u'4'))

        @UnicodeArguments([1])
        def f2(a, b, c):
            return a, b, c

        self.assertEqual(f2(1, 2, 3), (1, u'2', 3))
        self.assertEqual(f2(1, 2, c=4), (1, u'2', u'4'))
        self.assertEqual(f2(a=1, b=2, c=4), (u'1', u'2', u'4'))

        @UnicodeArguments([], 'b')
        def f2(a, b, c):
            return a, b, c

        self.assertEqual(f2(1, 2, 3), (1, 2, 3))
        self.assertEqual(f2(1, 2, c=4), (1, 2, 4))
        self.assertEqual(f2(1, b=2, c=4), (1, u'2', 4))

    def method_test(self):

        class A(object):

            @UnicodeArguments([1, 2, 3])
            def m1(self, a, b, c):
                assert isinstance(self, A)
                return a, b, c

            @UnicodeArguments()
            def m2(self, a, b, c):
                if not isinstance(self, A):
                    raise Exception('Bad self argument!')
                return a, b, c

            @UnicodeArguments(skip=['self', 0])
            def m3(self, a, b, c):
                assert isinstance(self, A)
                return a, b, c

            @UnicodeArguments(skip=['self', 0, 'b'])
            def m4(self, a, b, c):
                assert isinstance(self, A)
                return a, b, c

        a = A()

        self.assertEqual(a.m1(1, 2, 3), (u'1', u'2', u'3'))
        self.assertRaises(Exception, a.m2, 1, 2, 3)
        self.assertEqual(a.m3(1, 2, 3), (u'1', u'2', u'3'))
        self.assertEqual(a.m4(a=1, b=2, c=3), (u'1', 2, u'3'))
