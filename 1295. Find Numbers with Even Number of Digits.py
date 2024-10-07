"""Given an array nums of integers, return how many of them contain an even number of digits."""


def find_numbers(nums: list[int]) -> int:
    """
    :type nums: List[int]
    :rtype: int
    """
    tot_even = 0
    for i in nums:
        if len(str(i)) % 2 == 0:
            tot_even += 1
    return tot_even


"""Case Tests"""
example1 = [12,345,2,6,7896]  # Output: 2
"""Explanation:
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits."""

example2 = [555,901,482,1771]  # Output: 1
"""Explanation: 
Only 1771 contains an even number of digits."""

print(find_numbers(example1))
print(find_numbers(example2))