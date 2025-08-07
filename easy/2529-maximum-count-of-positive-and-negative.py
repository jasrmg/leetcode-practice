"""
2529. Maximum Count of Positive Integer and Negative Integer

Given an array nums sorted in non-decreasing order, return the maximum between 
the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number 
of negative integers is neg, then return the maximum of pos and neg.

Note that 0 is neither positive nor negative.

Constraints:
- 1 <= nums.length <= 1000
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.
"""

class Solution(object):
  def maximumCount(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    negative = 0
    positive = 0
    for num in nums:
      if num == 0:
        continue
      if num > 0:
        positive += 1
      else:
        negative += 1
    
    return max(positive, negative)
  

if __name__ == "__main__":
  obj = Solution()
  nums = [-3,-2,-1,0,0,1,2]
  print("MAX NUMBER OF POS AND NEG: ", obj.maximumCount(nums))