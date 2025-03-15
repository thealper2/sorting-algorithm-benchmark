"""
Bubble Sort Implementation

A simple comparison-based sorting algorithm that repeatedly steps through the list,
compares adjacent elements, and swaps them if they are in the wrong order.
"""

from typing import List


def sort(data: List[str]) -> List[str]:
    """
    Sort data using the Bubble Sort algorithm

    Args:
        data: List of strings to sort

    Returns:
        Sorted list of strings
    """
    # Create a copy to avoid modifying the original
    result = data.copy()
    n = len(result)

    # Optimization: flag to check if any swaps were made in an iteration
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if result[j] > result[j + 1]:
                # Swap if they are in the wrong order
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        # If no swapping occurred in this iteration, the array is sorted
        if not swapped:
            break

    return result
