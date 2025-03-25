# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
import unittest


def strStr(haystack: str, needle: str) -> int:
    index = -1
    if needle in haystack:
        index = haystack.index(needle)

    return index


"""Unit tests"""
class teststrStr(unittest.TestCase):
    def testExample1(self):
        self.assertEqual(strStr("sadbutsad", "sad"), 0)

    def testExample2(self):
        self.assertEqual(strStr("leetcode", "leeto"), -1)
