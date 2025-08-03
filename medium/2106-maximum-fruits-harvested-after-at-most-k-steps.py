# Problem: 2106. Maximum Fruits Harvested After at Most K Steps
# Link: https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/
# Difficulty: Medium
# Tags: Sliding Window, Binary Search, Greedy
# Language: Python

"""
Fruits are available at some positions on an infinite x-axis. You are given a 2D integer array `fruits` where 
fruits[i] = [position_i, amount_i] depicts `amount_i` fruits at the position `position_i`. `fruits` is already 
sorted by position_i in ascending order, and each position_i is unique.

You are also given an integer `startPos` and an integer `k`. Initially, you are at the position `startPos`. 
From any position, you can either walk to the left or right. It takes one step to move one unit on the x-axis, 
and you can walk at most `k` steps in total. For every position you reach, you harvest all the fruits at that 
position, and the fruits will disappear from that position.

Return the maximum total number of fruits you can harvest.

Example:
---------
Input: fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4  
Output: 9  
Explanation:  
- Move right to position 6 and harvest 3 fruits  
- Move right to position 8 and harvest 6 fruits  
You moved 3 steps and harvested 3 + 6 = 9 fruits in total.
"""

# solution starts here:
# time complexity: O(n^2)

class Solution(object):
  def maxTotalFruits(self, fruits, startPos, k):
    """
    :type fruits: List[List[int]]
    :type startPos: int
    :type k: int
    :rtype: int
    """
    n = len(fruits)
    max_fruits = 0

    for i in range(n):
      for j in range(i, n):
        left = fruits[i][0] # leftmost position
        right = fruits[j][0] # rightmost position

        steps_left_first = abs(startPos - left) + (right - left)
        steps_right_first = abs(startPos - right) + (right - left)

        # checks if its less <= k
        if min(steps_left_first, steps_right_first) <= k:
          total_fruits = sum(fruit[1] for fruit in fruits[i:j+1])
          max_fruits = max(max_fruits, total_fruits)
    
    return max_fruits
# ------------------------------------------------------------------------------------------------------  
# time complexity: O(n)
class OptimizedSolution(object):
  def maxTotalFruits(self, fruits, startPos, k):
    """
    :type fruits: List[List[int]]
    :type startPos: int
    :type k: int
    :rtype: int
    """
    n = len(fruits)
    max_fruits = 0
    total_fruits = 0
    left = 0

    for right in range(n):
      position, amount = fruits[right]
      total_fruits += amount # add current right positions fruits to window

      # Shrink the window from the left until it's valid (within k steps)
      while left <= right:
        left_position = fruits[left][0]
        right_position = fruits[right][0]

        # calculate min steps to collect all fruits from left to right
        steps_left_first = abs(startPos - left_position) + (right_position - left_position)
        steprs_right_first = abs(startPos - right_position) + (right_position - left_position)

        if min(steps_left_first, steprs_right_first) <= k:
          break # window is valid
        else:
          # window is invalid; remove left fruit and move window right
          total_fruits -= fruits[left][1]
          left += 1

      # Update max fruits harvested
      max_fruits = max(max_fruits, total_fruits)

    return max_fruits