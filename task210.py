from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
         # build adjacent list $ indegree list
        adjacent, indegree = {vertex: [] for vertex in range(numCourses)}, {vertex: 0 for vertex in range(numCourses)}
        for v, u in prerequisites: 
            adjacent[u].append(v)
            indegree[v] += 1
        head = [] # for those indgree = 0
        order = []
        num_visited = 0 # number of visited vertices
        for v in indegree: 
            if indegree[v] == 0: head.append(v)
        while head:
            current = head.pop(0)
            order.append(current)
            num_visited += 1
            for v in adjacent[current]:
                indegree[v] -= 1
                if indegree[v] == 0: head.append(v)
        if num_visited < numCourses: return []
        else: return order