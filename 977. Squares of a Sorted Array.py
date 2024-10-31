"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order."""


def sorted_squares(nums: list) -> list:
    n = len(nums)
    l_pointer, r_pointer = 0, n - 1
    result = [0] * n
    for i in range(n - 1, -1, -1):
        if abs(nums[l_pointer]) > abs(nums[r_pointer]):
            square = nums[l_pointer] * nums[l_pointer]
            l_pointer += 1
        else:
            square = nums[r_pointer] * nums[r_pointer]
            r_pointer -= 1
        
        result[i] = square
    
    return result


"""Test Cases"""
import unittest

class TestSortedSquares(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(sorted_squares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
    
    def test_ex2(self):
        self.assertEqual(sorted_squares([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])


if __name__ == '__main__':
    unittest.main()
