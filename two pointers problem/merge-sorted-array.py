"""
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, both sorted in non-decreasing order,
and two integers m and n, representing the number of valid elements in nums1 and nums2.

- nums1 has a length of m + n, where the first m elements are valid,
  and the last n elements are 0s as placeholders.
- nums2 has exactly n elements.

Your task is to merge nums2 into nums1 as one sorted array in-place.
Do not return anything — modify nums1 directly.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]

Constraints:
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10^9 <= nums1[i], nums2[j] <= 10^9

Follow up: Can you solve it in O(m + n) time using constant extra space?
"""
def merge(nums1, m, nums2, n):
  """
  m = number of element in the nums1 list
  n = number of element in the nums2 list
  """
  p1 = m - 1 # last index of n1
  p2 = n - 1 # last index of n2
  p = m + n - 1 # last index of n1

  while p1 >= 0 and p2 >= 0:
    if nums1[p1] > nums2[p2]:
      nums1[p] = nums1[p1]
      p1 -= 1
    else:
      nums1[p] = nums2[p2]
      p2 -= 1
    p -= 1
  
  while p2 >= 0:
    nums1[p] = nums2[p2]
    p2 -= 1
    p -= 1
  
  return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(merge([1], 1, [], 0))
print(merge([0], 0, [1], 1))
