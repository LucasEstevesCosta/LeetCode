import unittest

"""
Given a roman numeral, convert it to an integer.
"""

def romanToInt(s: str) -> int:
    pass


"""Unit Tests"""


class testRomanToInt(unittest.TestCase):
    def testExample1(self):
        self.assertEqual(romanToInt("III"), 3)
    
    def testExample2(self):
        self.assertEqual(romanToInt("LVIII"), 58)
    
    def testExample3(self):
        self.assertEqual(romanToInt("MCMXCIV"), 1994)
