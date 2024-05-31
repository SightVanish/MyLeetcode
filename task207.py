from typing import List
# DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacent list
        adjacent = {vertex: [] for vertex in range(numCourses)}
        for u, v in prerequisites: adjacent[u].append(v)
        state = {vertex: 0 for vertex in range(numCourses)} # 0: this vertex is unvisited; -1: being visited (not all descendants visited); 1: visited
        def hasCycle(vertex):
            if state[vertex] == 1: return False
            if state[vertex] == -1: return True
            state[vertex] = -1
            for descendant in adjacent[vertex]:
                if hasCycle(descendant): return True
            state[vertex] = 1
            return False
        for vertex in adjacent:
            if hasCycle(vertex): return False
        return True

# BFS - Topological sorting  
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacent list $ indegree list
        adjacent, indegree = {vertex: [] for vertex in range(numCourses)}, {vertex: 0 for vertex in range(numCourses)}
        for u, v in prerequisites: 
            adjacent[u].append(v)
            indegree[v] += 1
        head = [] # for those indgree = 0
        num_visited = 0 # number of visited vertices
        for v in indegree: 
            if indegree[v] == 0: head.append(v)
        while head:
            current = head.pop(0)
            num_visited += 1
            for v in adjacent[current]:
                indegree[v] -= 1
                if indegree[v] == 0: head.append(v)
        if num_visited < numCourses: return False
        else: return True

s = Solution()
print(s.canFinish(2, [[1,0],[0,1]]))