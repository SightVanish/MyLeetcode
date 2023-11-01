"""
You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:
pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
Note that ^ denotes the bitwise-xor operation.
It can be proven that the answer is unique.
"""

from typing import List
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]]
        for i in range(1, len(pref)):
            res.append(pref[i]^pref[i-1])
        return res
        

pref = [5,2,0,3,1]
s = Solution()
print(s.findArray(pref))

