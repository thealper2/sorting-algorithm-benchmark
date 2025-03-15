"""
Merge Sort Implementation

An efficient, stable, comparison-based, divide and conquer sorting algorithm.
It divides the input array into two halves, calls itself for the two halves,
and then merges the two sorted halves.
"""

from typing import List


def sort(data: List[str]) -> List[str]:
    """
    Sort data using the Merge Sort algorithm

    Args:
        data: List of strings to sort

    Returns:
        Sorted list of strings
    """
    # Create a copy to avoid modifying the original
    result = data.copy()

    if len(result) > 1:
        # Finding the middle of the array
        mid = len(result) // 2

        # Dividing the array elements into 2 halves
        L = result[:mid]
        R = result[mid:]

        # Sorting the halves
        L = sort(L)
        R = sort(R)

        # Initial indices for L, R and result arrays
        i = j = k = 0

        # Merge the two halves
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                result[k] = L[i]
                i += 1
            else:
                result[k] = R[j]
                j += 1
            k += 1

        # Check if any elements were left
        while i < len(L):
            result[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            result[k] = R[j]
            j += 1
            k += 1

    return result
