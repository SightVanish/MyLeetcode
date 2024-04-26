from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cost = [gas[i]-cost[i] for i in range(len(gas))]
        for i in range(len(cost)):
            temp = 0
            if cost[i] >= 0:
                for j in range(len(cost)):
                    temp += cost[(i+j)%len(cost)]
                    if temp < 0: break
                if temp >= 0: return i
        return -1


s = Solution()
print(s.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))



        