from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        # go through each bit
        for i in range(32):
            # count the number of 1s
            count = 0
            for n in nums: count += n >> i & 1
            # if count % 3 == 1, this extra 1 must be contributed by the single element
            if count % 3:
                mask = 1 << i
                res = res | mask # set the corresponding bit to 1
        return res if res < 2**31 else res - 2**32
            
s = Solution()
print(s.singleNumber([0,1,0,1,0,1,99]))
