import unittest


def removeDuplicates(nums: list[int]) -> int:
    unique = 1
    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[unique] = nums[i]
            unique += 1
    return unique


"""Unit tests"""


class TestRemoveDuplicates(unittest.TestCase):
    def testExample1(self):
        nums = [1, 1, 2]
        self.assertEqual(removeDuplicates(nums), 2)
        self.assertEqual(nums[:2], [1, 2])

    def testExample2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        numsProcessed = removeDuplicates(nums)
        self.assertEqual(numsProcessed, 5)
        self.assertEqual(nums[:numsProcessed], [0, 1, 2, 3, 4])
