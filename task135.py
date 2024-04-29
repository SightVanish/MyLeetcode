from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        c = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]: c[i] = c[i-1] + 1
            else: c[i] = 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]: c[i] = max(c[i], c[i+1]+1)
        return sum(c)

s = Solution()
print(s.candy([1,2,2]))                
