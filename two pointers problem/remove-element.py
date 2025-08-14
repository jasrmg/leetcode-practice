"""
27. Remove Element
Problem:
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` from `nums` in-place. 
The order of the remaining elements does not matter. The relative order can change.
Return the number of elements in `nums` that are not equal to `val`.

Requirements:
- Modify the array in-place so that the first k elements contain all the values not equal to `val`.
- The remaining elements beyond index k are not important.
- Return k (the count of non-val elements).

Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
class Solution():
  def remove_element(self, val, nums):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    left, right = 0, len(nums) - 1

    while left <= right:
      if nums[left] == val:
        nums[left] = nums[right]
        right -= 1
      else:
        left += 1
      
    return left
  
nums = [3,2,2,3] 
val = 3
re = Solution().remove_element
print(re(val, nums))