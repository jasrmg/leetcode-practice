"""
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
----------------------
Example 1:
Input: n = 1
Output: true
Explanation: 2^0 = 1
----------------------
Example 2:
Input: n = 16
Output: true
Explanation: 2^4 = 16
----------------------
Example 3:
Input: n = 3
Output: false
----------------------
Constraints: -2^31 <= n <= 2^31 - 1
"""
class Solution(object):
  def isPowerOfTwo(self, n):
    # A power of two has exactly one '1' in its binary form. 
    # n & (n - 1) clears the lowest '1'. 
    # If the result is 0 and n > 0, n is a power of two.
    return n > 0 and (n & (n - 1)) == 0
  