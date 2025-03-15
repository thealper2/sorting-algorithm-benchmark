"""
Heap Sort Implementation

A comparison-based sorting algorithm that uses a binary heap data structure.
It divides its input into a sorted and an unsorted region, and iteratively
shrinks the unsorted region by extracting the largest element and moving it
to the sorted region.
"""

from typing import List


def sort(data: List[str]) -> List[str]:
    """
    Sort data using the Heap Sort algorithm

    Args:
        data: List of strings to sort

    Returns:
        Sorted list of strings
    """
    # Create a copy to avoid modifying the original
    result = data.copy()
    n = len(result)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(result, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Swap the root (maximum element) with the last element
        result[i], result[0] = result[0], result[i]

        # Call max heapify on the reduced heap
        _heapify(result, i, 0)

    return result


def _heapify(arr: List[str], n: int, i: int) -> None:
    """
    Heapify a subtree rooted at index i

    Args:
        arr: List to heapify
        n: Size of the heap
        i: Root index of the subtree
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Heapify the affected sub-tree
        _heapify(arr, n, largest)
