"""
Problem: 2438. Range Product Queries of Powers

Given a positive integer n, represent it as a sorted array 'powers' containing the minimum number of powers of 2 that sum up to n.

You are given multiple queries [left, right], each asking for the product of elements in 'powers' from index left to right (inclusive), modulo 10^9 + 7.

Return a list of answers for each query.

Constraints:
- 1 <= n <= 10^9
- 1 <= number of queries <= 10^5
- 0 <= left <= right < len(powers)

Example:
Input: n = 15, queries = [[0,1],[2,2],[0,3]]
Output: [2,4,64]

Explanation:
For n=15, powers = [1, 2, 4, 8].
- Query [0,1]: product = 1 * 2 = 2
- Query [2,2]: product = 4
- Query [0,3]: product = 1 * 2 * 4 * 8 = 64
"""


class Solution(object):
  def productQueries(self, n, queries):
    """
    :type n: int
    :type queries: List[List[int]]
    :rtype: List[int]
    """

    mod = 10**9 + 7

    # Step 1. Build powers array from binary representation of n:
    powers =  []
    power = 1
    while n > 0:
      if n & 1:
        powers.append(power)
      n >>= 1
      power <<= 1
    
    # Step 2. Precompute prefix products
    prefix = [1] * (len(powers) + 1)
    for i in range(len(powers)):
      prefix[i + 1] = (prefix[i] * powers[i]) % mod

    # Step 3. Answer queries in O(1) each
    ans = []
    for left, right in queries:
      product = (prefix[right + 1] * pow(prefix[left], mod - 2, mod)) % mod
      ans.append(product)
    
    return ans
  
if __name__ == '__main__':
  obj = Solution()
  n = 15
  queries = [[0,1],[2,2],[0,3]]
  print(obj.productQueries(n, queries)) # Output: [2,4,64]