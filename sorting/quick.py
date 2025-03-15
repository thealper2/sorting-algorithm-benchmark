"""
Quick Sort Implementation

An efficient, in-place, comparison-based, divide and conquer sorting algorithm.
It works by selecting a 'pivot' element from the array and partitioning the other elements
into two sub-arrays according to whether they are less than or greater than the pivot.
"""

from typing import List
import random


def sort(data: List[str]) -> List[str]:
    """
    Sort data using the Quick Sort algorithm

    Args:
        data: List of strings to sort

    Returns:
        Sorted list of strings
    """
    # Create a copy to avoid modifying the original
    result = data.copy()

    # Call the quicksort helper function
    _quicksort(result, 0, len(result) - 1)

    return result


def _quicksort(arr: List[str], low: int, high: int) -> None:
    """
    Helper function for quicksort

    Args:
        arr: List to sort
        low: Starting index
        high: Ending index
    """
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = _partition(arr, low, high)

        # Sort the elements before and after the pivot
        _quicksort(arr, low, pivot_index - 1)
        _quicksort(arr, pivot_index + 1, high)


def _partition(arr: List[str], low: int, high: int) -> int:
    """
    Partition the array and return the pivot index

    Args:
        arr: List to partition
        low: Starting index
        high: Ending index

    Returns:
        Pivot index
    """
    # Use a random pivot to avoid worst-case performance on already sorted arrays
    pivot_idx = random.randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]

    pivot = arr[high]  # Choose the rightmost element as pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1  # Return the pivot index
