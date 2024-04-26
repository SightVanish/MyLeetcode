from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i in range(len(citations)):
            if citations[i] >= i+1: h += 1
            else: break
        return h

# introduce more space for speading
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = [0 for _ in range(len(citations)+1)]
        for i in range(len(citations)):
            h[min(citations[i], len(citations))] += 1
        index = 0
        for i in range(len(citations), -1, -1):
            index += h[i]
            if index >= i: return min(i, index)
        return index


s = Solution()
print(s.hIndex([1,1]))
