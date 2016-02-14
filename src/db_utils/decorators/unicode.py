#!/usr/bin/python


""" Decorators for converting to and from Unicode.
"""


def to_unicode(value, encoding='utf-8'):
    """ Converts value to Unicode.
    """

    if isinstance(value, bytes):
        return value.decode(encoding)
    else:
        return str(value)


def to_bytes(value, encoding='utf-8'):
    """ Converts value to byte string.
    """

    if isinstance(value, str):
        return value.encode(encoding)
    else:
        return bytes(value)


class UnicodeArguments(object):
    """ Decorator, which ensures, that function gets Unicode arguments.
    """

    def __init__(
            self, positional_arguments=None, keyword_arguments=None,
            skip=None):
        """

        +   ``positional_arguments`` -- list of integers, which says which
            positional arguments have to be Unicode;
        +   ``keyword_arguments`` -- list of strings, which says which
            keyword arguments have to be Unicode.
        +   ``skip`` -- list of arguments, which shouldn't be converted.
            If argument is integer, then positional argument is skipped,
            otherwise -- keyword.
        """

        self.positional_arguments = positional_arguments
        self.keyword_arguments = keyword_arguments
        self.skiped_positional_arguments = [
                arg for arg in skip or [] if isinstance(arg, int)]
        self.skiped_keyword_arguments = [
                arg for arg in skip or [] if not isinstance(arg, int)]

    def __call__(self, function):

        def wrapper(*args, **kwargs):
            """ Wrapper function, which converts arguments to unicode.
            """

            if self.positional_arguments is None:
                args = [
                        to_unicode(arg)
                        if i not in self.skiped_positional_arguments
                        else arg
                        for i, arg in enumerate(args)
                        ]
            else:
                args = list(args)
                for position in self.positional_arguments:
                    if (position < len(args) and
                        position not in self.skiped_positional_arguments):

                        args[position] = to_unicode(args[position])

            if self.keyword_arguments is None:
                kwargs = dict([
                    (key, to_unicode(arg))
                    if key not in self.skiped_keyword_arguments
                    else (key, arg)
                    for key, arg in kwargs.items()
                    ])
            else:
                for key in self.keyword_arguments:
                    if (key in kwargs.keys() and
                        key not in self.skiped_keyword_arguments):

                        kwargs[key] = to_unicode(kwargs[key])

            return function(*args, **kwargs)

        return wrapper
