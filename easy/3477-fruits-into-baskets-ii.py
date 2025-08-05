# Problem: 3477. Fruits Into Baskets II
# Link: https://leetcode.com/problems/fruits-into-baskets-ii/
# Difficulty: Easy
# Tags: Greedy, Arrays
# Language: Python

"""
You are given two arrays of integers, `fruits` and `baskets`, each of length `n`, where 
`fruits[i]` represents the quantity of the ith type of fruit, and `baskets[j]` represents 
the capacity of the jth basket.

From left to right, place the fruits according to these rules:

1. Each fruit type must be placed in the **leftmost available basket** with a capacity 
   greater than or equal to the quantity of that fruit type.
2. Each basket can hold only **one type of fruit**.
3. If a fruit type cannot be placed in any basket, it remains unplaced.

Return the **number of fruit types that remain unplaced** after all possible allocations are made.

Examples:
---------
Input: fruits = [4, 2, 5], baskets = [3, 5, 4]  
Output: 1  
Explanation:
- fruits[0] = 4 → baskets[1] = 5
- fruits[1] = 2 → baskets[0] = 3
- fruits[2] = 5 → cannot fit in basket[2] = 4 → unplaced

Input: fruits = [3, 6, 1], baskets = [6, 4, 7]  
Output: 0  
Explanation:
- fruits[0] = 3 → basket[0] = 6
- fruits[1] = 6 → basket[2] = 7
- fruits[2] = 1 → basket[1] = 4
"""
# solution starts here:
# time complexity
class Solution(object):
  def numOfUnplacedFruits(self, fruits, baskets):
    """
      :type fruits: List[int]
      :type baskets: List[int]
      :rtype: int
    """
    n = len(fruits)
    used = [False] * n
    unplaced = 0

    for i in range(n): # loop through the fruits array
      placed = False # flag to check if the fruit is placed or not
      for j in range(n): # loop through the baskets array
        if not used[j] and baskets[j] >= fruits[i]: # checks if the basket is not occupied and is greater than the # of fruits
          used[j] = True
          placed = True
          break
      
      if not placed: # if the fruit is not placed inside a basket
        unplaced += 1

    return unplaced


  
if __name__ == '__main__':
  obj = Solution()
  print(obj.numOfUnplacedFruits([4,2,5], [3,5,4])) # 1
  print(obj.numOfUnplacedFruits([3,6,1], [6,4,7])) # 0

