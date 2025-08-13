##############################################################################
#
# Copyright (c) 2001 Mark Pilgrim and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Convert to and from Roman numerals"""

__author__ = "Mark Pilgrim (f8dy@diveintopython.org)"
__copyright__ = """Copyright (c) 2001 Mark Pilgrim

This program is part of "Dive Into Python", a free Python tutorial for
experienced programmers.  Visit http://diveintopython.org/ for the
latest version.
"""

import argparse
import re
import sys


# Define exceptions
class RomanError(Exception):
    pass


class OutOfRangeError(RomanError):
    pass


class NotIntegerError(RomanError):
    pass


class InvalidRomanNumeralError(RomanError):
    pass


# Define digit mapping
romanNumeralMap = (('M', 1000),
                   ('CM', 900),
                   ('D', 500),
                   ('CD', 400),
                   ('C', 100),
                   ('XC', 90),
                   ('L', 50),
                   ('XL', 40),
                   ('X', 10),
                   ('IX', 9),
                   ('V', 5),
                   ('IV', 4),
                   ('I', 1))


def toRoman(n: int) -> str:
    """convert integer to Roman numeral"""
    if not isinstance(n, int):
        raise NotIntegerError("decimals cannot be converted")
    if not (-1 < n < 5000):
        raise OutOfRangeError("number out of range (must be 0..4999)")

    # special case
    if n == 0:
        return 'N'

    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result


# Define pattern to detect valid Roman numerals
romanNumeralPattern = re.compile("""
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """, re.VERBOSE)


def fromRoman(s: str, special_case: bool = True) -> int:
    """
    Convert Roman numeral to integer.

    Parameters:
        s (str): The Roman numeral string to convert.
        special_case (bool, optional): If True (default),
            interprets 'N' as 0 for the special case of zero.

    Returns:
        int: The integer value of the Roman numeral.

    Raises:
        InvalidRomanNumeralError: If the input is not a valid Roman numeral.
    """

    if not s:
        raise InvalidRomanNumeralError('Input cannot be blank')

    s = s.upper()  # Handle lowercase inputs

    # special case
    if s == 'N' and special_case:
        return 0

    if not romanNumeralPattern.search(s):
        raise InvalidRomanNumeralError('Invalid Roman numeral: %s' % s)

    result = 0
    index = 0
    for numeral, integer in romanNumeralMap:
        while s[index:index + len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='roman',
        description='convert between roman and arabic numerals'
    )
    parser.add_argument('number', help='the value to convert')
    parser.add_argument(
        '-r', '--reverse',
        action='store_true',
        default=False,
        help='convert roman to numeral (case insensitive) [default: False]')

    args = parser.parse_args()
    args.number = args.number
    return args


def main() -> int:
    args = parse_args()
    if args.reverse:
        r = fromRoman(args.number)
        print(r)
    else:
        i = int(args.number)
        n = toRoman(i)
        print(n)

    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())  # pragma: no cover
