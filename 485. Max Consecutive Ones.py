"""Given a binary array nums, return the maximum number of consecutive 1's in the array."""
from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    tot_temp = 0
    tot_final = 0
    for n in nums:
        if n == 1:
            tot_temp += 1
            tot_final = max(tot_final, tot_temp)
        else:
            tot_temp = 0
    return tot_final


# Test
example1 = [1, 1, 0, 1, 1, 1]  # Output: 3
example2 = [1, 0, 1, 1, 0, 1]  # Output: 2
example3 = [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1]

print(findMaxConsecutiveOnes(example1))
print(findMaxConsecutiveOnes(example2))
print(findMaxConsecutiveOnes(example3))
