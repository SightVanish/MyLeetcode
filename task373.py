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
        heap = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if len(heap) < k: heapq.heappush(heap, (-(nums1[i] + nums2[j]), nums1[i], nums2[j]))
                elif -(nums1[i] + nums2[j]) > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-(nums1[i] + nums2[j]), nums1[i], nums2[j]))
                else: break
        return [i[1:] for i in heap]
s = Solution()
print(s.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))