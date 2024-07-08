from typing import List
from collections import defaultdict

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        if len(set(nums)) == len(nums) or len(set(nums)) == 1: return len(nums)
        res = 0
        frequency = defaultdict(int)
        count_frequency = defaultdict(int)
        max_frequency = 0
        for j in range(len(nums)):
            count_frequency[frequency[nums[j]]] -= 1
            if count_frequency[frequency[nums[j]]] <= 0: del count_frequency[frequency[nums[j]]]
            frequency[nums[j]] += 1
            max_frequency = max(max_frequency, frequency[nums[j]])
            count_frequency[frequency[nums[j]]] += 1
            # eg. 111 222 333 4
            if max_frequency * count_frequency[max_frequency] == j: res = j + 1
            # eg. 11 22 33 44 555
            if (max_frequency - 1) * count_frequency[max_frequency - 1] + (max_frequency - 1) == j: res = j + 1
        return res
    
s = Solution()
print(s.maxEqualFreq([1,1,1,2,2,2]))
        
