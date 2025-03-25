def heightChecker(heights: list[int]) -> int:
    """
    Determines the number of students that are not standing in their correct positions.

    This function takes a list of heights representing the heights of students in a line. 
    It compares the original list with a sorted version of the heights to identify the 
    number of students who need to swap positions to be in ascending order.

    Args:
        heights (list[int]): A list of integers representing the heights of students.

    Returns:
        int: The number of students that need to change their positions to be in order.

    Examples:
        >>> heightChecker([1, 1, 4, 2, 1, 3])
        3
        >>> heightChecker([5, 1, 2, 3, 4])
        5
        >>> heightChecker([1, 2, 3, 4, 5])
        0
    """
    # Create expected array with heights sorted in increasing order
    expected = sorted(heights)
    
    t = 0 # Númber of different indexes
    # Compare the two arrays
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            t += 1
        
    # Return number of different indexes
    return t


import unittest

class TestHeightChecker(unittest.TestCase):
    """
    Unit tests for the heightChecker function.
    """
    def test_empty_list(self):
        """
        Tests the function with an empty list.
        """
        self.assertEqual(heightChecker([]), 0)

    def test_unsorted_list(self):
        """
        Tests the function with an unsorted list.
        """
        self.assertEqual(heightChecker([1, 1, 4, 2, 1, 3]), 3)

    def test_unsorted_list2(self):
        """
        Tests the function with a different unsorted list.
        """
        self.assertEqual(heightChecker([5, 1, 2, 3, 4]), 5)
    
    def test_sorted_list(self):
        """
        Tests the function with a sorted list.
        """
        self.assertEqual(heightChecker([1, 2, 3, 4, 5]), 0)

    def test_duplicate_heights(self):
        """
        Tests the function with a list containing duplicate heights.
        """
        self.assertEqual(heightChecker([1, 1, 1, 2, 2]), 0)

if __name__ == '__main__':
    unittest.main()
