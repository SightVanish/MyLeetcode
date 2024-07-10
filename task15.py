# 3 Sum
from typing import List

# fix one number and what left is a twoSum question
# O(n) space, O(n2) time
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort nums first
        res = set()
        # fixed i and search for j, k
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    res.add((nums[i], nums[j], nums[k])) # must use set + tuple to remove duplicates and ensure time complexity
                    j += 1
                    k -= 1
                elif s > 0: k -= 1
                elif s < 0: j += 1
        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        negatives, positives, zeros = [], [], []
        for i in nums:
            if i < 0: negatives.append(i)
            elif i > 0: positives.append(i)
            else: zeros.append(i)

        # case: (0, 0, 0)
        if len(zeros) >= 3: res.add((0, 0, 0))

        # case: (num, 0, -num)
        n, p = set(negatives), set(positives)
        if zeros:
            for i in n:
                if -i in p: res.add((0, i, -i))
        
        # case (-x, -y, z) with 2 negative elements
        for i in range(len(negatives)):
            for j in range(i + 1, len(negatives)):
                target = -negatives[i]-negatives[j]
                if target in p: res.add(tuple(sorted([negatives[i], negatives[j], target]))) # sorted-> remove duplicated

        # case (x, y, -z) with 2 positive elements
        for i in range(len(positives)):
            for j in range(i + 1, len(positives)):
                target = -positives[i]-positives[j]
                if target in n: res.add(tuple(sorted([target, positives[i], positives[j]])))
        
        return res


s = Solution()
res = s.threeSum([2,1,3,4])
print(res)
