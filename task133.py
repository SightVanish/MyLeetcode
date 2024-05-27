
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None
        unvisited, visited = [node], {}
        while unvisited:
            current = unvisited.pop()
            visited[current] = Node(current.val)
            for i in current.neighbors: 
                if i not in visited: unvisited.append(i)
        for n in visited:
            visited[n].neighbors = [visited[i] for i in n.neighbors]
        return list(visited.values())[0]

p1 = Node(1)
p2 = Node(2)
p3 = Node(3)
p4 = Node(4)
p1.neighbors = [p2, p4]
p2.neighbors = [p1, p3]
p3.neighbors = [p2, p4]
p4.neighbors = [p1, p3]

s = Solution()
print(p1)
print(s.cloneGraph(p1))