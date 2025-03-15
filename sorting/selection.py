"""
Selection Sort Implementation

A simple comparison-based sorting algorithm that divides the input list into a sorted
and an unsorted region, and repeatedly finds the minimum element in the unsorted region
and moves it to the sorted region.
"""

from typing import List


def sort(data: List[str]) -> List[str]:
    """
    Sort data using the Selection Sort algorithm

    Args:
        data: List of strings to sort

    Returns:
        Sorted list of strings
    """
    # Create a copy to avoid modifying the original
    result = data.copy()
    n = len(result)

    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the unsorted part
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        result[i], result[min_idx] = result[min_idx], result[i]

    return result
