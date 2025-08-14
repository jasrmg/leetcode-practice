"""
Given an integer array nums, move all 0's to the end of the array while maintaining the relative order 
of the non-zero elements.

The operation must be done in-place, without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
"""

def moveZeroes(nums):
  last_non_zero = 0

  for i in range(len(nums)):
    if (nums[i] != 0):
      nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
      last_non_zero += 1
    
  return nums

nums = [0,1,0,3,12]
print(moveZeroes(nums))
    