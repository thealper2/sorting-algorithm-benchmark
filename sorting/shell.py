"""
Shell Sort Implementation

An in-place comparison sort that generalizes insertion sort by allowing the exchange
of items that are far apart. It starts by sorting pairs of elements far apart from
each other, then progressively reduces the gap between elements to be compared.
"""

from typing import List


def sort(data: List[str]) -> List[str]:
    """
    Sort data using the Shell Sort algorithm

    Args:
        data: List of strings to sort

    Returns:
        Sorted list of strings
    """
    # Create a copy to avoid modifying the original
    result = data.copy()
    n = len(result)

    # Start with a big gap, then reduce the gap
    # Using the Sedgewick sequence for gap values
    gaps = [1, 4, 10, 23, 57, 132, 301, 701, 1750]

    # Find the largest gap that is smaller than n
    gap_index = len(gaps) - 1
    while gap_index >= 0 and gaps[gap_index] >= n:
        gap_index -= 1

    # Do a gapped insertion sort for this gap size
    while gap_index >= 0:
        gap = gaps[gap_index]

        # Do the insertion sort for this gap size
        for i in range(gap, n):
            # Save a copy of the element to be inserted
            temp = result[i]

            # Shift earlier gap-sorted elements up until the correct location is found
            j = i
            while j >= gap and result[j - gap] > temp:
                result[j] = result[j - gap]
                j -= gap

            # Put temp in its correct location
            result[j] = temp

        gap_index -= 1

    return result
