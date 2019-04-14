import unittest
import roman

TEST_MAP = ((0, 'N'), (1, 'I'), (3, 'III'), (4, 'IV'), (9, 'IX'), (14, 'XIV'),
            (19, 'XIX'), (24, 'XXIV'), (40, 'XL'), (49, 'XLIX'), (90, 'XC'),
            (99, 'XCIX'), (400, 'CD'), (490, 'CDXC'), (499, 'CDXCIX'),
            (900, 'CM'), (990, 'CMXC'), (998, 'CMXCVIII'), (999, 'CMXCIX'),
            (2013, 'MMXIII'))

class TestRoman(unittest.TestCase):

    def test_toRoman(self):
        for num_arabic, num_roman in TEST_MAP:
            self.assertEqual(roman.toRoman(num_arabic), num_roman,
                             '%s should be %s' % (num_arabic, num_roman))

    def test_toRoman_errors(self):
        self.assertRaises(roman.OutOfRangeError, roman.toRoman, 100000)
        self.assertRaises(roman.NotIntegerError, roman.toRoman, '1')

    def test_fromRoman(self):
        for num_arabic, num_roman in TEST_MAP:
            self.assertEqual(roman.fromRoman(num_roman), num_arabic,
                             '%s should be %s' % (num_roman, num_arabic))

    def test_fromRoman_errors(self):
        self.assertRaises(
            roman.InvalidRomanNumeralError, roman.fromRoman, '')
        self.assertRaises(
            roman.InvalidRomanNumeralError, roman.fromRoman, 'Q12')

def test_suite():
    return unittest.makeSuite(TestRoman)
