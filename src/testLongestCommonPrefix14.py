import unittest

""" https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ''
    if len(strs) <= 1:
        return strs[0]
    
    prefix = strs[0]
    for i in range(1, len(strs)):
        j = 0
        while j < len(prefix) and j < len(strs[i]) and prefix[j] == strs[i][j]:
            j += 1
        prefix = prefix[:j]

    return prefix


""" Unit Tests """

class TestlongestCommonPrefix(unittest.TestCase):
    def testExample1(self):
        self.assertEqual(longestCommonPrefix(["flower","flow","flight"]), "fl")
    
    def testExample2(self):
        self.assertEqual(longestCommonPrefix(["dog","racecar","car"]), "")
