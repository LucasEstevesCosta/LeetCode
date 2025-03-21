def remove_duplicates(nums: list[int]) -> int:
    i = 0
    for n in range(1, len(nums)):
        if nums[n] != nums[i]:
            i += 1
            nums[i] = nums[n]
    return i + 1


"""TEST CASES"""
example1 = [1, 1, 2]
"""Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores)."""

example2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
"""Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores)."""

k1 = remove_duplicates(example1)
print(f"k1 = {k1}, example1 = {example1[:k1]}")

k2 = remove_duplicates(example2)
print(f"k2 = {k2}, example2 = {example2[:k2]}")
