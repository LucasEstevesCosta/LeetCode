"""Given a binary array nums, return the maximum number of consecutive 1's in the array."""

def find_max_consecutive_ones(nums: list[int]) -> int:



"""TESTS"""
import unittest

class test_find_max_consecutive_ones(unittest.TestCase):
    def test_ex1(self):
        self.assertEquals(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]), 3)

    def test_ex2(self):
        self.assertEquals(find_max_consecutive_ones([1, 0, 1, 1, 0, 1]), 2)

# Test
example1 = [1, 1, 0, 1, 1, 1]  # Output: 3
example2 = [1, 0, 1, 1, 0, 1]  # Output: 2
example3 = [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1]
