def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    a = m - 1
    b = n - 1
    c = m + n - 1
    while b >= 0:
        if a >= 0 and nums1[a] > nums2[b]:
            nums1[c] = nums1[a]
            a -= 1
        else:
            nums1[c] = nums2[b]
            b -= 1
        c -= 1


"""Test Cases"""
# EXAMPLE 1
print('Example 1 | Output: [1,2,2,3,5,6]')
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(f'Resposta: {nums1}')
print()

# EXAMPLE 2
print('Example 2 | Output: [1]')
nums1 = [1]
m = 1
nums2 = []
n = 0

merge(nums1, m, nums2, n)
print(f'Resposta: {nums1}')
print()

# EXAMPLE 3
print('Example 3 | Output: [1]')
nums1 = [0]
m = 0
nums2 = [1]
n = 1

merge(nums1, m, nums2, n)
print(f'Resposta: {nums1}')
print()

# EXAMPLE 4
print('Example 4')
nums1 = [4, 0, 0, 0, 0, 0]
m = 1
nums2 = [1, 2, 3, 5, 6]
n = 5

merge(nums1, m, nums2, n)
print(f'Resposta: {nums1}')