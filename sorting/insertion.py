"""
Insertion Sort Implementation

A simple comparison-based sorting algorithm that builds the sorted list one item at a time.
It is efficient for small data sets and is often used as part of more sophisticated algorithms.
"""

from typing import List


def sort(data: List[str]) -> List[str]:
    """
    Sort data using the Insertion Sort algorithm

    Args:
        data: List of strings to sort

    Returns:
        Sorted list of strings
    """
    # Create a copy to avoid modifying the original
    result = data.copy()
    n = len(result)

    # Traverse through 1 to n
    for i in range(1, n):
        key = result[i]

        # Move elements of result[0..i-1] that are greater than key
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key

    return result
