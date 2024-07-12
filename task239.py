from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        res = []
        for i in range(len(nums)):
            # if the last element of queue < next element, there is no need to track this element
            while queue and nums[i] > queue[-1]: queue.pop()
            queue.append(nums[i])
            # if the max value remove the element not in the sliding window anymore
            if i >= k and nums[i - k] == queue[0]: queue = queue[1:]
            # the first element in queue is guaranteed to be the max one
            if i >= k - 1: res.append(queue[0])
        return res

s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))