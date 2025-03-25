"""Given a fixed-length integer array arr, duplicate each occurrence of zero,
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place and do not return anything."""


def duplicate_zeros(arr: list[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    n = len(arr)
    zeros = arr.count(0)

    for i in range(n - 1, -1, -1):  # i = 0 / zero = 0 / len = 8
        if i + zeros < n:
            arr[i + zeros] = arr[i]

        if arr[i] == 0:
            zeros -= 1
            if i + zeros < n:
                arr[i + zeros] = 0


"""Test Cases"""
example1 = [1, 0, 2, 3, 0, 4, 5, 0]  # Output: [1, 0, 0, 2, 3, 0, 0, 4]
# Explanation: After calling your function, the input array is modified to: [1, 0, 0, 2, 3, 0, 0, 4]

example2 = [1, 2, 3]  # Output: [1, 2, 3]
# Explanation: After calling your function, the input array is modified to: [1, 2, 3]

duplicate_zeros(example1)
duplicate_zeros(example2)
print(example1)
print(example2)
