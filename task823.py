"""
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.
We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.
Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

Example 1:
Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]

Example 2:
Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
"""

from typing import List
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        num = {i: 1 for i in arr} # num of binary tree for the case when each element be the root
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in arr: # this line is very important. finding interger in a arr is much more faster than finding a float in arr (about 2x faster)
                    num[arr[i]] += num[arr[j]] * num[arr[i] // arr[j]]
        return sum(num.values()) % (10**9 + 7)

s = Solution()
print(s.numFactoredBinaryTrees([2,4,5,10]))


        