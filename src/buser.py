"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
"""
from math import floor, ceil


# Array Merge
# Merge Otimization
# Return Median
# num1 = [1, 3]


def arrays_median(num1, num2):
    num1.extend(num2)
    num1.sort()
    length = len(num1)


    if length % 2 == 0:
        median_pos_init = int(length / 2 - 1)
        median_pos_end = int(length / 2)
        return (num1[median_pos_init] + num1[median_pos_end]) / 2

    median_pos = floor(len(num1) / 2)

    return num1[median_pos]


# num1 = [1, 2, 3]

assert arrays_median([1, 3], [2]) == 2
assert arrays_median([1, 2], [3, 4]) == 2.5
assert arrays_median([0, 0], [0, 0]) == 0
assert arrays_median([1, 3], [2, 4, 5])
