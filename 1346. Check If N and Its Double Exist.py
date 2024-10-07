def checkIfExist(arr: list[int]) -> bool:
    """
    Given a list of integers arr, determine whether there exists a pair of numbers
    where one number is double the other.

    Args:
        arr: A list of integers.

    Returns:
        True if there exists a pair of numbers where one number is double the other, 
        False otherwise.
    """
    seen = set()
    for num in arr:
        if num * 2 in seen or (num % 2 == 0 and num / 2 in seen):
            return True
        seen.add(num)
    return False


"""TEST CASES"""
example1 = [10,2,5,3] # Output: true
"""Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]"""

example2 = [3,1,7,11] # Output: false
"""Explanation: There is no i and j that satisfy the conditions."""

example3 = [7,1,14,11] # Output: true
"""Explanation: There is no i and j that satisfy the conditions."""

example4 = [0,0] # Output: true
"""Explanation: There is no i and j that satisfy the conditions."""

print(f'{checkIfExist(example1)} OUTPUT: True')
print(f'{checkIfExist(example2)} OUTPUT: False')
print(f'{checkIfExist(example3)} OUTPUT: True')
print(f'{checkIfExist(example4)} OUTPUT: True')
