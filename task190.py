class Solution:
    def reverseBits(self, n: int) -> int:
        return int('0b' + bin(n)[2:][::-1] + '0'*(34-len(bin(n))), 2)

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) + (n & 1)
            n = n >> 1
        return res
    
s = Solution()
print(s.reverseBits(43261596))