def thirdMax(nums: list[int]) -> int:
    """
    Finds the third largest number in a list of integers.

    Args:
        nums (list[int]): A list of integers.

    Returns:
        int: The third largest number in the list, or the largest number if there are fewer than three distinct numbers.

    Examples:
        >>> thirdMax([3, 2, 1])
        1
        >>> thirdMax([1, 2, 2])
        2
        >>> thirdMax([2, 2, 3, 1])
        1
    """
    # Create a set of unique numbers to remove duplicates
    unique_nums = set(nums)
    
    # If there are fewer than three distinct numbers, return the largest number
    if len(unique_nums) < 3:
        return max(unique_nums)
    
    # Initialize the maximum values
    first_max = float('-inf')
    second_max = float('-inf')
    third_max = float('-inf')
    
    # Iterate through the unique numbers
    for number in unique_nums:
        # If the current number is greater than the first maximum, update the maximums
        if number > first_max:
            third_max = second_max
            second_max = first_max
            first_max = number
        # If the current number is greater than the second maximum but not the first maximum, update the maximums
        elif number > second_max and number != first_max:
            third_max = second_max
            second_max = number
        # If the current number is greater than the third maximum and not the first or second maximum, update the third maximum
        elif number > third_max and number != first_max and number != second_max:
            third_max = number
        
    # Return the third maximum if it exists, otherwise return the first maximum
    return third_max


import unittest

class TestThirdMax(unittest.TestCase):
    
    def test_ex1(self):
        self.assertEqual(thirdMax([3,2,1]), 1)
        """The first distinct maximum is 3.
            The second distinct maximum is 2.
            The third distinct maximum is 1."""
    
    def test_ex2(self):
        self.assertEqual(thirdMax([1,2]), 2)
        """The first distinct maximum is 2.
            The second distinct maximum is 1.
            The third distinct maximum does not exist, so the maximum (2) is returned instead."""
    
    def test_ex3(self):
        self.assertEqual(thirdMax([2,2,3,1]), 1)
        """The first distinct maximum is 3.
            The second distinct maximum is 2 (both 2's are counted together since they have the same value).
            The third distinct maximum is 1."""
            
    def test_ex4(self):
        self.assertEqual(thirdMax([1, 1, 2]), 2)
        
    def test_ex5(self):
        self.assertEqual(thirdMax([1,2,-2147483648]), -2147483648)

if __name__ == '__main__':
    unittest.main()
