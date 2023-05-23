"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

# a better solution is to solve via collections.Counter and min heap (keep track of the k_th most frequent element)
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d[i] + 1 if i in d else 1
        d = list(zip(list(d.keys()), list(d.values())))
        d = sorted(d, key=lambda x: x[1], reverse=True)
        return [x[0] for x in d[:k]]

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         frequency = {}
#         for i in nums:
#             if i in frequency:
#                 frequency[i] += 1
#             else:
#                 frequency[i] = 1
#         max_frequence = max(frequency.values())
#         bucket = [[] for i in range(max_frequence + 1)]
#         for key in frequency:
#             bucket[frequency[key]].append(key)
#         ans = []
#         j = max_frequence

#         # print(bucket)
#         while k > 0:
#             while len(bucket[j]) == 0:
#                 j -= 1
#             if len(bucket[j]) > k:
#                 ans += (bucket[j][:k])
#             ans += (bucket[j])
#             k -= len(bucket[j])
#             j -= 1

#         return ans


s = Solution()
print(s.topKFrequent([1,2], 2))
