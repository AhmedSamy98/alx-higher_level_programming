#!/usr/bin/python3
"""
Find the peak in an unordered list of integers using binary search
"""

def find_peak(list_of_integers):
    """
    Find the peak in a list of integers using binary search.

    Args:
        list_of_integers (list): List of integers.

    Returns:
        int: The peak integer.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = left + (right - left) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # If the current element is greater than the next element, move left
            right = mid
        else:
            # Otherwise, move right
            left = mid + 1

    # At the end of the loop, left and right will converge to the peak element
    return list_of_integers[left]

# Example usage:
if __name__ == "__main__":
    test_list = [1, 3, 20, 4, 1, 0]
    result = find_peak(test_list)
    print("Peak element:", result)

