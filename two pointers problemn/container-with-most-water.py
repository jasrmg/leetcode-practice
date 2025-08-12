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
