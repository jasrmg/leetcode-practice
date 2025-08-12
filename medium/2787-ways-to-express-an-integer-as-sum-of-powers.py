"""
Problem: 2787. Ways to Express an Integer as Sum of Powers

Given two integers n and x, count the number of ways to represent n as the sum of unique
positive integers each raised to the xth power. Return the answer modulo 10^9 + 7.

Approach:
- Precompute all possible powers <= n (i^x where i >= 1).
- Use dynamic programming where dp[k] represents the number of ways to form sum k
  using the available powers.
- Initialize dp[0] = 1 (one way to make sum 0: choose nothing).
- For each power, iterate through sums from n down to power to update dp.
- Take modulo 10^9 + 7 at each addition to prevent overflow.

Time Complexity: O(m * n), where m is the number of powers <= n.
Space Complexity: O(n), storing the dp array.

Example:
n = 10, x = 2
Powers = [1, 4, 9]
Ways to form 10:
- 1^2 + 3^2 = 10
Output: 1
"""


class Solution(object):
  def numberOfWays(self, n, x):
    MOD = 10**9 + 7
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
      val = i**x
      for j in range(n + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= val:
          dp[i][j] = (dp[i][j] + dp[i - 1][j - val]) % MOD
    
    return dp[n][n]
  
  