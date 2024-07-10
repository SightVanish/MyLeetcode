from heapq import heapify, heappop, heappush
class Solution:
    def largestInteger(self, num: int) -> int:
        nums = str(num)
        odd = []
        even = []
        res = []
        for i in nums:
            if int(i) % 2: heappush(odd, -int(i))
            else: heappush(even, -int(i))
        for i in range(len(nums)):
            if int(nums[i]) % 2: res.append(str(-heappop(odd)))
            else: res.append(str(-heappop(even)))
        return int(''.join(res))
