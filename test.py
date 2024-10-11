"""ARQUIVO QUE USO PARA TESTAR ALGUMAS COISAS"""
def removeElement(nums: list[int], val: int) -> int:
    pi = 0
    pf = len(nums) - 1
    while pi <= pf:
        if nums[pi] == val:
            if nums[pf] != val:
                nums[pi], nums[pf] = nums[pf], nums[pi]
                pf -= 1
                pi += 1
            else:
                pf -= 1
        else:
            pi += 1
        
    return pi
        
"""TEST CASES"""
example1 = [3, 2, 2, 3]
val1 = 3
"""Output: 2, nums = [2, 2, _, _]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores)."""

example2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
"""Output: 5, nums = [0, 1, 4, 0, 3, _, _, _]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores)."""

k1 = removeElement(example1, val1)
print(f"k1 = {k1}, example1 = {example1[:k1]}; EXPECTED OUTPUT: [2, 2]")

k2 = removeElement(example2, val2)
print(f"k2 = {k2}, example2 = {example2[:k2]}; EXPECTED OUTPUT: [0, 1, 4, 0, 3]")
