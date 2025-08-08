"""
LeetCode 3363: Find the Maximum Number of Fruits Collected

You are given a 2D array `fruits` of size n x n, where fruits[i][j] represents
the number of fruits in the room (i, j). Three children start at the following corners:

- Child A starts at (0, 0)
- Child B starts at (0, n - 1)
- Child C starts at (n - 1, 0)

Each child will make exactly (n - 1) moves to reach the bottom-right cell (n - 1, n - 1).
They move according to specific rules:

- Child A can move to (i+1, j), (i, j+1), or (i+1, j+1)
- Child B can move to (i+1, j), (i+1, j-1), or (i+1, j+1)
- Child C can move to (i-1, j+1), (i, j+1), or (i+1, j+1)

When a child enters a room, they collect all the fruits in it. 
If two or more children enter the same room, only one collects the fruits, and the room is emptied.

Return the maximum number of fruits the children can collect.

Constraints:
- 2 <= n == fruits.length == fruits[i].length <= 1000
- 0 <= fruits[i][j] <= 1000
"""

class Solution:
  def maxCollectedFruits(self, fruits):
    n = len(fruits)
    ans = sum(fruits[i][i] for i in range(n))

    def dp():
      prev = [float("-inf")] * n
      curr = [float("-inf")] * n
      prev[n - 1] = fruits[0][n - 1]
      for i in range(1, n - 1):
        for j in range(max(n - 1 - i, i + 1), n):
          best = prev[j]
          if j - 1 >= 0:
            best = max(best, prev[j - 1])
          if j + 1 < n:
            best = max(best, prev[j + 1])
          curr[j] = best + fruits[i][j]
        prev, curr = curr, prev
      return prev[n - 1]

    ans += dp()

    for i in range(n):
      for j in range(i):
        fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]

    ans += dp()
    return ans
    

