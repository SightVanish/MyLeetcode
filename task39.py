from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        n = len(candidates)
        def trackback(curr, k, remains):
            if remains == 0: output.append(curr[:])
            else:
                for i in range(k, n):
                    if remains - candidates[i] >= 0: trackback(curr+[candidates[i]], i, remains-candidates[i])
        trackback([], 0, target)
        return output