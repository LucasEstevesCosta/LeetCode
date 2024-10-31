"""Given an array nums of integers, return how many of them contain an even number of digits."""


import unittest


def find_numbers(nums: list[int]) -> int:
    """
    :type nums: List[int]
    :rtype: int
    """
    tot_nums_even_digits = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            tot_nums_even_digits += 1
    return tot_nums_even_digits


# TEST CASES


class TestFindNumbers(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(find_numbers([12, 345, 2, 6, 7896]), 2)

    def test_ex2(self):
        self.assertEqual(find_numbers([555, 901, 482, 1771]), 1)


if __name__ == '__main__':
    unittest.main()
