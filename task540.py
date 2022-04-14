from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
        nums = [3,3,7,7,10,11,11]
        [3 3 7 7] [10 11 11]
        [10 11] [11]
        '''
        l, r, m = 0, len(nums)-1, 0
        while (l < r):
            m = l + (r-l)//2
            if m % 2 == 1:
                m -= 1
            if nums[m] == nums[m+1]:
                l = m + 2
            else:
                r = m

        return nums[l]

nums = [1,1,2,3,3,4,4,8,8]
ans = Solution()
print(ans.singleNonDuplicate(nums))
    
    