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

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        while i < len(gas):
            g = gas[i]
            for j in range(len(gas)):
                if g >= cost[(i+j)%len(cost)]: g += gas[(i+j+1)%len(cost)] - cost[(i+j)%len(cost)]
                else:
                    # if the car stoped at i+j, then all nodes between i and i+j will not be considered
                    i += j + 1
                    break
                if j == len(gas)-1: return i
        return -1


s = Solution()
print(s.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))



        