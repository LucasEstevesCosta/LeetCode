import unittest

"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""


def isPalindrome(x: int) -> bool:
    num = x
    reversedNum = 0

    while num > 0:
        digit = num % 10
        reversedNum = reversedNum * 10 + digit
        num = num // 10

    if reversedNum == x:
        return True
    else:
        return False


"""Unit tests"""


class TestIsPalindrome(unittest.TestCase):
    def testExample1(self):
        self.assertEqual(isPalindrome(121), True)
    
    def testExample2(self):
        self.assertEqual(isPalindrome(-121), False)

    def testExample3(self):
        self.assertEqual(isPalindrome(10), False)
