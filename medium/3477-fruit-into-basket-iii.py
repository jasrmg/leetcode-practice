# Problem: 3479. Fruits Into Baskets III
# Link: https://leetcode.com/problems/fruits-into-baskets-iii/
# Difficulty: Medium
# Tags: Greedy, Two Pointers, Sqrt Decomposition
# Language: Python

"""
You are given two arrays of integers, `fruits` and `baskets`, each of length `n`, where:
- `fruits[i]` represents the quantity of the ith type of fruit,
- `baskets[j]` represents the capacity of the jth basket.

Starting from the left, place the fruits into baskets using the following rules:
1. Each fruit type must be placed in the **leftmost available basket** with a capacity **greater than or equal** to that fruit type.
2. Each basket can hold only **one type** of fruit.
3. If a fruit type cannot be placed in any basket, it remains unplaced.

Return the number of fruit types that remain unplaced after all possible allocations are made.

Example 1:
----------
Input: fruits = [4,2,5], baskets = [3,5,4]
Output: 1
Explanation:
- Fruit 4 goes to basket 5 (index 1)
- Fruit 2 goes to basket 3 (index 0)
- Fruit 5 can't fit into the remaining basket 4 (index 2)

Example 2:
----------
Input: fruits = [3,6,1], baskets = [6,4,7]
Output: 0
Explanation:
- Fruit 3 → basket 6 (index 0)
- Fruit 6 → basket 7 (index 2)
- Fruit 1 → basket 4 (index 1)
All fruits are placed successfully.
"""


# solution that passed the test cases(4649ms):
import math

class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        sect_mx = []
        m = len(baskets)
        a = int(math.sqrt(m))  # size of one array

        cnt = 0
        mx = 0
        for i in range(m):
            if cnt == a:
                # creating sector of size a
                sect_mx.append(mx)
                mx = baskets[i]
                cnt = 1
            else:
                cnt += 1
                mx = max(mx, baskets[i])

        # last sector
        sect_mx.append(mx)

        remain = 0

        # start allocating
        for fruit in fruits:
            k = 0
            set_flag = 1

            for j in range(0, m, a):
                if sect_mx[k] < fruit:
                    # skip this segment
                    k += 1
                    continue

                # find place to allocate
                for r in range(j, min(j + a, m)):
                    if baskets[r] >= fruit:
                        set_flag = 0
                        baskets[r] = 0
                        break

                # if fruit is allocated in a sector
                if set_flag == 0:
                    sect_mx[k] = 0  # find new mx
                    # update new sector mx
                    for r in range(j, min(j + a, m)):
                        sect_mx[k] = max(baskets[r], sect_mx[k])
                    break

                k += 1

            remain += set_flag

        return remain