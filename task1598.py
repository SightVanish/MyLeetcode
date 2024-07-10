from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for i in logs:
            if i == "../": 
                if res > 0: res -= 1
            elif i == "./": pass
            else: res += 1
        return res
s = Solution()
print(s.minOperations(["./","../","./"]))