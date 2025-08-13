"""
1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:
Input: nums = [1, 2, 3, 4], k = 5
Output: 2
Explanation:
- Remove numbers 1 and 4 → nums = [2, 3]
- Remove numbers 2 and 3 → nums = []
No more pairs sum to k, so total operations = 2.

Example 2:
Input: nums = [3, 1, 3, 4, 3], k = 6
Output: 1
Explanation:
- Remove the first two 3's → nums = [1, 4, 3]
No more pairs sum to k.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= 10^9
"""

class Solution(object):
  def max_operations(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums.sort()
    i, j = 0, len(nums) - 1
    count = 0

    while i < j:
      total = nums[i] + nums[j]
      if total == k:
        count += 1
        i += 1
        j -= 1
      elif total < k:
        i += 1
      else:
        j -= 1
    
    return count
  
print(Solution().max_operations([1, 2, 3, 4], 5))