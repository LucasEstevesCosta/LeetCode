def sorted_squares(nums: list) -> list:
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    """result = list()
    for i in nums:
        result.append(i * i)
    return sorted(result)"""
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            square = nums[left] * nums[left]
            left += 1
        else:
            square = nums[right] * nums[right]
            right -= 1
        result[i] = square
    return result


"""Test Cases"""
example1 = [-4, -1, 0, 3, 10]  # Output: [0, 1, 9, 16, 100]
# Explanation: After squaring, the array becomes [16, 1, 0, 9, 100].
# After sorting, it becomes [0, 1, 9, 16, 100].
example2 = [-7, -3, 2, 3, 11]  # Output: [4, 9, 9, 49, 121]

print(sorted_squares(example1))
print(sorted_squares(example2))
