"""
Bucket Sort Implementation for Strings

A distribution sort that works by distributing the elements into a number of buckets,
then sorting each bucket individually. This implementation is adapted for strings.
"""

from typing import List


def sort(data: List[str]) -> List[str]:
    """
    Sort data using the Bucket Sort algorithm for strings

    Args:
        data: List of strings to sort

    Returns:
        Sorted list of strings
    """
    # Create a copy to avoid modifying the original
    result = data.copy()

    if len(result) <= 1:
        return result

    # Create buckets based on the first letter of each string
    # For Unicode support, we'll use 27 buckets (a-z + others)
    buckets = [[] for _ in range(27)]

    # Distribute items into buckets
    for item in result:
        if item and item[0].isalpha():
            # Calculate index based on the first letter (case insensitive)
            index = ord(item[0].lower()) - ord("a")
            buckets[index].append(item)
        else:
            # Items that don't start with a letter go to the last bucket
            buckets[26].append(item)

    # Sort individual buckets using insertion sort
    for i in range(27):
        buckets[i] = _insertion_sort(buckets[i])

    # Concatenate all buckets
    result.clear()
    for bucket in buckets:
        result.extend(bucket)

    return result


def _insertion_sort(arr: List[str]) -> List[str]:
    """
    Helper function for insertion sort

    Args:
        arr: List to sort

    Returns:
        Sorted list
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
