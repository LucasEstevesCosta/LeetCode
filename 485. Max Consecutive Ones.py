"""Given a binary array nums, return the maximum number of consecutive 1's in the array."""
import unittest


def find_max_consecutive_ones(nums: list[int]) -> int:
    temp_counter = 0
    final_counter = 0
    for index, num in enumerate(nums):
        if num == 1:
            temp_counter += 1
        if num == 0 or index == len(nums) - 1:
            if temp_counter > final_counter:
                final_counter = temp_counter
            temp_counter = 0
    return final_counter


"""TESTS"""


class Test_find_max_consecutive_ones(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]), 3)

    def test_ex2(self):
        self.assertEqual(find_max_consecutive_ones([1, 0, 1, 1, 0, 1]), 2)


if __name__ == '__main__':
    unittest.main()
