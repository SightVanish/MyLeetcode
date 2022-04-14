from cmath import inf
from typing import List
"""
O(n^2)
"""
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                tmp = nums[j]-nums[i]
                ans = tmp if tmp > ans else ans
        return ans if ans > 0 else -1

"""
O(n)
for each i, the possible j must be the max one
"""
class Solution1:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0, len(nums)-1):
            tmp = max(nums[i+1:])-nums[i]
            ans = tmp if tmp > ans else ans
        return ans if ans > 0 else -1

s = Solution1()
nums = [999,997,980,976,948,940,938,928,924,917,907,907,881,878,864,862,859,857,848,840,824,824,824,805,802,798,788,777,775,766,755,748,735,732,727,705,700,697,693,679,676,644,634,624,599,596,588,583,562,558,553,539,537,536,509,491,485,483,454,449,438,425,403,368,345,327,287,285,270,263,255,248,235,234,224,221,201,189,187,183,179,168,155,153,150,144,107,102,102,87,80,57,55,49,48,45,26,26,23,15]
print(s.maximumDifference(nums))
