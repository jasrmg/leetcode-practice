# Problem: 904. Fruit Into Baskets
# Link: https://leetcode.com/problems/fruit-into-baskets/
# Difficulty: Medium
# Tags: Sliding Window, Two Pointers
# Language: Python

"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. 
The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit 
the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules:

- You only have two baskets, and each basket can only hold a single type of fruit. 
- There is no limit on the amount of fruit each basket can hold.
- Starting from any tree of your choice, you must pick exactly one fruit from every tree 
  (including the start tree) while moving to the right.
- The picked fruits must fit in one of your baskets.
- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Return the maximum number of fruits you can pick.

Example:
---------
Input: fruits = [1,2,1]  
Output: 3  
Explanation: We can pick from all trees.

Input: fruits = [0,1,2,2]  
Output: 3  
Explanation: Pick from index 1 to index 3 (fruits = [1,2,2]).
"""


# solution starts here:
# time complexity: 0(n), space complexity: 0(1)
class Solution:
  def totalFruits(self, fruits: list[int]) -> int: # type hint
    from collections import defaultdict # used to store the fruit counts efficiently

    basket = defaultdict(int) # holds the current fruit type in the window
    left = 0
    max_fruits = 0

    #1. step through each tree from left to right
    for right in range(len(fruits)):
      #2. add the current fruit at 'right' into the basket
      basket[fruits[right]] += 1

      #3. check if we have more than 2 types in the basket
      while len(basket) > 2:
        #too many types - shrink down the basket
        basket[fruits[left]] -= 1

        # if count becomes zero, remove that fruit type from the basket
        if basket[fruits[left]] == 0:
          del basket[fruits[left]]

        # move left boundary forward
        left += 1
      
      #4. update the maximum fruits collected so far
      # current window size is right - left + 1
      max_fruits = max(max_fruits, right - left + 1)

    return max_fruits
  
if __name__ == "__main__":
  print("hello world")

  obj = Solution()
  fruits = [1, 2, 1, 3, 1, 2]

  print("MAX FRUITS: ", obj.totalFruits(fruits))