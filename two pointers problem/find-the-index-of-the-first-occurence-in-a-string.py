"""
Problem: 28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack.
If needle is not part of haystack, return -1.

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0.

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode".

Constraints
1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.
"""

def strStr(haystack, needle):
  n, m = len(haystack), len(needle)
  if m == 0:
    return 0
  
  i, j = 0, 0

  while i < n:
    if haystack[i] == needle[j]:
      i += 1
      j += 1
      if j == m:
        return i - m
    else:
      i = i - j + 1
      j = 0
  return -1


# haystack = "sadbutsad" 
# needle = "sad"
haystack = "0leetcode" 
needle = "leet"
print(strStr(haystack, needle))