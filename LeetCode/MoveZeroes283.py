def moveZeroes(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        wp = 0 # WritePointer
        for i in range(len(nums)): # Iterar na lista com o ReadPointer range(0, len(nums))
            if nums[i] != 0: # Se ElementoAtual == 0
                nums[wp] = nums[i] # Substitui WritePointer por ElementoAtual
                wp += 1 # WritePointer += 1
        for i in range(wp, len(nums)): # Iterar na lista range(WritePoint, len(nums))
            nums[i] = 0 # ElementoAtual = 0
        return nums
    
    
"""TEST CASES"""
example1 = [0,1,0,3,12] # Output: [1, 3, 12, 0, 0]
example2 = [0] # Output: [0]
    
moveZeroes(example1)
moveZeroes(example2)

print(f'Result: {example1}; Expected Result: [1, 3, 12, 0, 0]')
print(f'Result: {example2}; Expected Result: [0]')
