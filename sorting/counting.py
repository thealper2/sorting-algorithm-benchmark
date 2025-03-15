"""
Counting Sort Implementation for Strings

A non-comparative sorting algorithm that operates by counting the number of objects
that have each distinct key value. This implementation is adapted for strings by
using the first character as the key.
"""

from typing import List


def sort(data: List[str]) -> List[str]:
    """
    Sort data using the Counting Sort algorithm

    Args:
        data: List of strings to sort

    Returns:
        Sorted list of strings
    """
    # For string sorting, we'll use a modified approach
    # First, group strings by their first character
    buckets = {}

    # Create a copy to avoid modifying the original
    result = data.copy()

    # Handle empty list
    if not result:
        return result

    # Group strings by first character
    for s in result:
        # Use first character as key, or empty string for empty strings
        key = s[0] if s else ""
        if key not in buckets:
            buckets[key] = []
        buckets[key].append(s)

    # Sort the keys (first characters)
    sorted_keys = sorted(buckets.keys())

    # Reconstruct the sorted list
    sorted_result = []
    for key in sorted_keys:
        # Sort strings within each bucket
        bucket = sorted(buckets[key])
        sorted_result.extend(bucket)

    return sorted_result
