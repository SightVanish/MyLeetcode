"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
"""
from typing import List
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        i = 0
        for n1 in nums1:
            for n2 in nums2:
                if i < k:
                    heapq.heappush(res, (-(n1+n2), [n1, n2]))
                    i += 1
                else:
                    if -res[0][0] <= n1 + n2: break
                    else:
                        heapq.heappop(res)
                        heapq.heappush(res, (-(n1+n2), [n1, n2]))
        return [i[1] for i in res]
s = Solution()
print(s.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))





