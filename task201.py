# bit and -> find the common prefix
# for the rest bits, there is no way be 1 (only if the bit of all integer between left and right be 1, this bit can be 1)
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count += 1
        return left << count
        

s = Solution()
print(s.rangeBitwiseAnd(left = 1, right = 2147483647))