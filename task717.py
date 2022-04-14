from curses.ascii import SO
from re import S
from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        ans = True
        while i < len(bits):
            if bits[i] == 1:
                i += 2
                ans = False
            else:
                i += 1
                ans = True
        return ans

            
s = Solution()

bits = [1,0,0]

print(s.isOneBitCharacter(bits))
