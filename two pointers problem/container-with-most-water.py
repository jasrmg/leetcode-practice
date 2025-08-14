"""
You are given an integer array height of length n. There are n vertical lines drawn such that
the two endpoints of the i-th line are (i, 0) and (i, height[i]).

Find two lines that, together with the x-axis, form a container that can store the most water.

Return the maximum amount of water a container can store.

Note:
- The container sides must be vertical (you may not slant the container).
- The width of the container is the distance between the two chosen lines.
- The height of the container is determined by the shorter of the two lines.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation:
The maximum area is obtained by choosing height[1] = 8 and height[8] = 7.
Area = min(8, 7) * (8 - 1) = 7 * 7 = 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""


def max_area(height):
  left, right = 0, len(height) - 1
  max_area = 0

  while left < right:
    width = right - left
    min_height = min(height[right], height[left])
    area = width * min_height
    max_area = max(max_area, area)

    if height[left] < height[right]:
      left += 1
    else:
      right -= 1
  
  return max_area

height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))


"""
OPTIMIZED VERSION: skipping the heights that wont improve the results
"""
def max_area_optimized(height):
  left, right = 0, len(height) - 1
  max_area = 0

  while left < right:
    min_height = min(height[left], height[right])
    width = right - left
    max_area = max(max_area, width * min_height)

    if height[left] < height[right]:
      curr = height[left]
      while left < right and height[left] <= curr:
        left += 1
    else:
      curr = height[right]
      while left < right and height[right] <= curr:
        right -= 1  
  
  return max_area

print(max_area_optimized(height))