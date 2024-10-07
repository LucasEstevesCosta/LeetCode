"""Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""

def twoSum(nums, target):
    for n in range(len(nums)):
        for i in range(n + 1, len(nums)):
            if nums[n] + nums[i] == target:
                return [n, i]


"""Pra testar"""
example1 =[[2,7,11,15], 9]  # Output: [0,1]
example2 = [[3,2,4], 6]  # Output: [1,2]
example3 = [[3,3], 6]  # Output: [0,1]

print(twoSum(example1[0], example1[1]))
print(twoSum(example2[0], example2[1]))
print(twoSum(example3[0], example3[1]))
