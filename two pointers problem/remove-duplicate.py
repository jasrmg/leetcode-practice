"""
26. Remove Duplicates from Sorted Array
Given a sorted array nums in non-decreasing order, remove the duplicates in-place such that each unique 
element appears only once. The relative order of the elements must remain the same.

After removing duplicates, return the number of unique elements k. The first k elements of nums should 
contain the unique elements in the order they appeared in nums initially. The elements beyond index k-1 
are not important.

Constraints:
    1 <= nums.length <= 3 * 10^4
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.

Example:
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Explanation:
    The function should return k = 5, with the first 5 elements of nums being the unique elements.
    The underscores represent values that can be ignored.
"""
class Solution():
  def remove_duplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    for j in range(1, len(nums)):
      if nums[i] != nums[j]:
        i += 1
        nums[i] = nums[j]
    
    return i + 1
  
rd = Solution().remove_duplicate
nums = [0,0,1,1,1,2,2,3,3,4]
print(rd(nums))