"""
Radix Sort Implementation for Strings

A non-comparative sorting algorithm that sorts data with integer keys by grouping keys
by individual digits which share the same significant position and value.
This implementation is adapted for strings.
"""

from typing import List


def sort(data: List[str]) -> List[str]:
    """
    Sort data using the Radix Sort algorithm for strings

    Args:
        data: List of strings to sort

    Returns:
        Sorted list of strings
    """
    # Create a copy to avoid modifying the original
    result = data.copy()

    # Find the maximum length string
    max_len = 0
    for item in result:
        max_len = max(max_len, len(item))

    # Pad strings with spaces to make them all the same length
    padded = [(s.ljust(max_len), i) for i, s in enumerate(result)]

    # Do counting sort for every character from right to left
    for pos in range(max_len - 1, -1, -1):
        # Initialize count array
        count = [0] * 256  # ASCII characters

        # Count occurrences of each character at current position
        for item, _ in padded:
            count[ord(item[pos])] += 1

        # Update count[i] to position of character in output
        for i in range(1, 256):
            count[i] += count[i - 1]

        # Build the output array
        output = [None] * len(padded)
        for i in range(len(padded) - 1, -1, -1):
            item, original_idx = padded[i]
            char_code = ord(item[pos])
            output[count[char_code] - 1] = padded[i]
            count[char_code] -= 1

        # Copy the output array to padded for next iteration
        padded = output

    # Reconstruct the original array (unpadded and in sorted order)
    return [result[original_idx] for _, original_idx in padded]
