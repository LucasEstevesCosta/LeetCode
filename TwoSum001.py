import unittest

"""Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""


def twoSum(nums, target):
    for p1 in range(len(nums)):
        for p2 in range(p1 + 1, len(nums)):
            if nums[p1] + nums[p2] == target:
                return [p1, p2]


"""Pra testar"""
example1 = [[2, 7, 11, 15], 9]  # Output: [0,1]
example2 = [[3, 2, 4], 6]  # Output: [1,2]
example3 = [[3, 3], 6]  # Output: [0,1]

print(twoSum(example1[0], example1[1]))
print(twoSum(example2[0], example2[1]))
print(twoSum(example3[0], example3[1]))

"""Unit Tests"""


class testTwoSuns(unittest.TestCase):
    def testExample1(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1])

    def testExample2(self):
        self.assertEqual(twoSum([3, 2, 4], 6), [1, 2])

    def testExample3(self):
        self.assertEqual(twoSum([3, 3], 6), [0, 1])


if __name__ == '__main__':
    unittest.main()
