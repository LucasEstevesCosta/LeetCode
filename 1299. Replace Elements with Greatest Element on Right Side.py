def replaceElements(arr: list[int]) -> list[int]:
    """
    Replaces each element in an array with the greatest element to its right.

    Args:
        arr: The input array.

    Returns:
        The modified array with elements replaced as described.
    """
    n = len(arr)
    if n == 0:
        return arr  # Empty array, nothing to do
    
    # Find the maximum element from right to left
    max_right = arr[n - 1]
    arr[n - 1] = -1 # Replace the last element with -1
    
    # Iterate from second-last element to the beginning
    for i in range(n - 2, -1, -1):
        # Store the current element
        temp = arr[i]
        # Replace the current element with the maximum seen so far
        arr[i] = max_right
        # Update the maximum element if the current element is greater
        if temp > max_right:
            max_right = temp
        
    return arr


"""Test Cases"""
example1 = [17, 18, 5, 4, 6, 1] # Output: [18, 6, 6, 6, 1, -1]
example2 = [400] # Output: [-1]
replaceElements(example1)
replaceElements(example2)
print(f'RESULT: {example1}; EXPECTED OUTPUT: [18, 6, 6, 6, 1, -1]')
print(f'RESULT: {example2}; EXPECTED OUTPUT: [-1]')
