"""
Given an integer n, you must transform it into 0 using the following operations any number of times:
Change the rightmost (0th) bit in the binary representation of n.
Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
Return the minimum number of operations to transform n into 0.
"""

# assumption 1: for input: n=2^k, it takes 2^(k+1)-1 steps to become 0
# proof via mathmatical induction: n can be presented as 10...0 (num of 0 is k)
#                                  as assumption it takes 2^k-1 steps to convert 01...0 to 0 and also it takes 2^k-1 steps to convert 0 to 01...0
#                                  so for 10...0 -> it takes 2^k-1 steps to become 11...0 -> it takes 1 step to become 01...0 -> it takes 2^k-1 steps to become 0
#                                  in total, it takes 2^k-1+1+2^k-1 = 2^(k+1)-1 steps
# why we need flip flag? take 1110 as example:
# 1000 takes 2^4-1 to become 0
# but sine the 2^nd bit is 1, it do not need convert 0 to 100 --> still for 100, it do not need to convert 0 to 10
# so it takes 2^4-1 save (2^3-1 in which also save 2^2-1) --> the total would be (2^4-1) - ((2^3-1) - (2^2-1))

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        flip = 0
        # go from left to right to check each leading 1
        for i in range(31, -1, -1):
            if (n >> i) & 1 == 1:
                if flip:
                    ans -= 2**(i+1) - 1
                    flip = 0
                else:
                    ans += 2**(i+1) - 1
                    flip = 1
        return ans
        
