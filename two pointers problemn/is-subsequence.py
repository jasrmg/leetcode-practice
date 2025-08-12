"""
Given two strings s and t, return True if s is a subsequence of t, or False otherwise.

A subsequence of a string is a new string formed from the original string by deleting 
some (can be none) of the characters without disturbing the relative positions of 
the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: True

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: False

Constraints:
0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.
"""

def is_subsequence(s, t):
  i, j = 0, 0

  while i < len(s) and j < len(t):
    if (s[i] == t[j]):
      i += 1
    j += 1
  
  return i == len(s)

s = "axc"
t = "ahbgdc"
print(is_subsequence(s, t))