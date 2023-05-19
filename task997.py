"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2
"""

from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0: return 1
        candidates = set(range(1, n+1))
        candidates -= set([i[0] for i in trust])
        candidates = dict.fromkeys(candidates, 0)
        for t in trust:
            if t[1] in candidates: 
                candidates[t[1]] += 1
                if candidates[t[1]] == n - 1: 
                    return t[1]
        
        return -1




s = Solution()
print(s.findJudge(n = 1, trust = []))