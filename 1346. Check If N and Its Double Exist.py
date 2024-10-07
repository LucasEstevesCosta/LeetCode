def checkIfExist(arr: list[int]) -> bool:


"""TEST CASES"""
example1 = [10,2,5,3] # Output: true
"""Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]"""

example2 = [3,1,7,11] # Output: false
"""Explanation: There is no i and j that satisfy the conditions."""

print(checkIfExist(example1))
print(checkIfExist(example2))
