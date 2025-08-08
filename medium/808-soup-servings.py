"""
LeetCode Problem 808: Soup Servings
Difficulty: Medium

You have two types of soup: A and B. Each starts with 'n' milliliters. At each turn, you randomly perform one of four operations with equal probability (0.25), where each operation removes a fixed amount of soup from A and B:

  - Serve 100 ml from A and 0 ml from B
  - Serve 75 ml from A and 25 ml from B
  - Serve 50 ml from A and 50 ml from B
  - Serve 25 ml from A and 75 ml from B

If a serving tries to remove more soup than is available, only the remaining amount is served. The process stops when either soup A or B is empty.

Return the probability that soup A becomes empty before soup B, plus half the probability that both soups become empty at the same time. Answers within 1e-5 of the correct result are accepted.

Constraints:
- 0 <= n <= 10^9

Optimization:
For large values of 'n' (>= 5000), the result approaches 1.0, and computation can be short-circuited for performance.
"""
class Solution(object):
  def soupServings(self, n):
    """
    :type n: int
    :rtype: float
    """

    # for large n, probability is approaches 1.0
    if n >= 4800:
      return 1.0
    
    # reduce state space by dividing 25 (gcd)
    n = (n + 24) // 25

    # memoization using dict
    memo = {}

    # recursive function to calculate the probability for (a, b) units left in Soup A and B
    def dp(a, b):
      if a <= 0 and b <= 0:
        return 0.5
      if a <= 0:
        return 1.0
      if b <= 0:
        return 0
      
      if (a, b) in memo:
        return memo[(a, b)]
      
      # operations in terms of the reduced units / 25
      prob = .25 * (
        dp(a - 4, b) +
        dp(a - 3, b - 1) +
        dp(a - 2, b - 2) +
        dp(a - 1, b - 3)
      )

      memo[(a, b)] = prob
      return prob
    
    return dp(n, n)
    