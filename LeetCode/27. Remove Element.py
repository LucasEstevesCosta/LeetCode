def remove_element(nums: list[int], val: int) -> int:
    k = 0
    for num in nums:
        if num != val:
            nums[k] = num
            k += 1
    return k


"""TEST CASES"""
example1 = [3, 2, 2, 3]
val1 = 3
"""Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores)."""

example2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
"""Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores)."""

k1 = remove_element(example1, val1)
print(f"k1 = {k1}, example1 = {example1[:k1]}")

k2 = remove_element(example2, val2)
print(f"k2 = {k2}, example2 = {example2[:k2]}")
