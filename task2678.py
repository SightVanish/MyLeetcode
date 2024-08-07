from typing import List
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for i in details:
            if int(i[-4:-2]) > 60: ans += 1
        return ans