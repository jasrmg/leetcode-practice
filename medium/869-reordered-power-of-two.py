"""
LeetCode 869 - Reordered Power of 2

You are given an integer n.
You can reorder the digits of n in any order (including keeping the same order),
but the resulting number cannot have a leading zero.

Return True if and only if we can reorder the digits to form a power of two.

A power of two is any number of the form 2^x where x >= 0, e.g. 1, 2, 4, 8, 16, 32, etc.

Constraints:
1 <= n <= 10^9

Example 1:
Input: n = 1
Output: True

Example 2:
Input: n = 10
Output: False
"""

# time complexity: O(1), space complexity: O(1)
class Solution(object):
  def reorderedPowerOf2(self, n):
    """
    :type n: int
    :rtype: bool
    """
    # step 1. GET THE SORTED DIGIT PATTERNS OF N (e.g., 128 -> ('1', '2', '8')) 
    target = tuple(sorted(str(n))) 

    # step 2. PRECOMPUTE SORTED DIGITS PATTERNS FOR ALL POWERS OF TWO
    # 2^0 to 2^30 covers all powers of two <= 10^9
    power_of_twos = {tuple(sorted(str(1 << i))) for i in range(31)}

    # step 3. CHECK IF n's DIGIT PATTERN IS IN THE SET(power_of_twos)
    return target in power_of_twos


if __name__ == '__main__':
  print("Hello World")
  obj = Solution()
  n = 128
  print(obj.reorderedPowerOf2(n))