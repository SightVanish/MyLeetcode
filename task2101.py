"""
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.
The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.
You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.
Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.
Example 1:
Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.
"""

from typing import List
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # build graph
        graph = {}
        for i in range(len(bombs)):
            graph[i] = []
            for j in range(len(bombs)):
                if i == j: continue
                if (bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2 <= bombs[i][2]**2:
                    graph[i] += [j]
        # run dfs on each nodes
        def dfs(i):
            d, visited = [i], []
            while d:
                i = d[0]
                d = d[1:]
                visited += [i]
                for j in graph[i]:
                    if j not in visited and j not in d:
                        d.append(j)
            return len(visited)
        res = 0
        for i in range(len(graph)):
            res = max(res, dfs(i))
        return res


s = Solution()
print(s.maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))


