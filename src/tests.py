import unittest
import roman

class TestRoman(unittest.TestCase):

    def test_toRoman(self):
        self.assertEqual(roman.toRoman(1), 'I')
        self.assertEqual(roman.toRoman(2013), 'MMXIII')

    def test_toRoman_errors(self):
        self.assertRaises(roman.OutOfRangeError, roman.toRoman, 100000)
        self.assertRaises(roman.NotIntegerError, roman.toRoman, '1')

    def test_fromRoman(self):
        self.assertEqual(roman.fromRoman('I'), 1)
        self.assertEqual(roman.fromRoman('MMXIII'), 2013)

    def test_fromRoman_errors(self):
        self.assertRaises(
            roman.InvalidRomanNumeralError, roman.fromRoman, '')
        self.assertRaises(
            roman.InvalidRomanNumeralError, roman.fromRoman, 'Q12')

def test_suite():
    return unittest.makeSuite(TestRoman)
