import unittest

"""
Given a roman numeral, convert it to an integer.
"""

def romanToInt(s: str) -> int:
    result = 0
    valueTable = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    i = 0
    while i < len(s):
        if i + 1 < len(s) and ((s[i] == "I" and s[i + 1] == "V") or (s[i] == "I" and s[i + 1] == "X") or
                                (s[i] == "X" and s[i + 1] == "L") or (s[i] == "X" and s[i + 1] == "C") or
                                (s[i] == "C" and s[i + 1] == "D") or (s[i] == "C" and s[i + 1] == "M")):
                result += valueTable[s[i + 1]] - valueTable[s[i]]
                i += 2
        else:
            result += valueTable[s[i]]
            i += 1

    return result


"""Unit Tests"""


class testRomanToInt(unittest.TestCase):
    def testExample1(self):
        self.assertEqual(romanToInt("III"), 3)
    
    def testExample2(self):
        self.assertEqual(romanToInt("LVIII"), 58)
    
    def testExample3(self):
        self.assertEqual(romanToInt("MCMXCIV"), 1994)
