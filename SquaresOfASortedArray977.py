"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order."""
import unittest


def sorted_squares(nums: list) -> list:
    n = len(nums)
    result = [0] * n
    right_pointer = n - 1
    left_pointer = 0
    for index in range(n - 1, -1, -1):
        if abs(nums[left_pointer]) > abs(nums[right_pointer]):
            square = nums[left_pointer] * nums[left_pointer]
            left_pointer += 1
        else:
            square = nums[right_pointer] * nums[right_pointer]
            right_pointer -= 1
        result[index] = square

    return result


"""Test Cases"""


class TestSortedSquares(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(sorted_squares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])

    def test_ex2(self):
        self.assertEqual(sorted_squares([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])


if __name__ == '__main__':
    unittest.main()
