"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.
"""
# using dict
class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        d = [[i, d[i]] for i in d]
        d.sort(key=lambda x:x[1], reverse=True)
        d = [i[0]*i[1] for i in d]
        return ''.join(d)
import heapq
# using heap
class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        res = ''
        for i in s:
            d[i] = d.get(i, 0) + 1
        d = [[-d[i], i] for i in d]
        heapq.heapify(d)
        while d:
            i, j = heapq.heappop(d)
            res += j*-i
        return res

s = Solution()
print(s.frequencySort('tree'))