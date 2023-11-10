"""
There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.
You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.
It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.
Return the original array nums. If there are multiple solutions, return any of them.
"""
from typing import List
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if len(adjacentPairs) <= 1: return adjacentPairs[0]
        res = []
        # build graph
        pair_dict = {}
        for pair in adjacentPairs:
            if pair[0] in pair_dict: pair_dict[pair[0]].append(pair[1])
            else: pair_dict[pair[0]] = [pair[1]]
            if pair[1] in pair_dict: pair_dict[pair[1]].append(pair[0])
            else: pair_dict[pair[1]] = [pair[0]]

        # find beginning node
        current, before = None, None
        for key in pair_dict.keys():
            if len(pair_dict[key]) == 1: current = key
        res.append(current)
        for _ in range(len(adjacentPairs)):
            next = pair_dict[current]
            current, before = next[0] if next[0] != before else next[1], current
            res.append(current)
        return res


s = Solution()
print(s.restoreArray([[4,-2],[1,4],[-3,1]]))