from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build a graph: graph[numerator] = [(denominator, fraction)]
        graph, res = {}, []
        for (numerator, denomintor), fraction in zip(equations, values):
            # a/b = x also refers b/a = 1/x
            if numerator in graph: graph[numerator].append([denomintor, fraction]) 
            else: graph[numerator] = [[denomintor, fraction]]
            if denomintor in graph: graph[denomintor].append([numerator, 1.0/fraction]) 
            else: graph[denomintor] = [[numerator, 1.0/fraction]]

        def searchGraph(numerator, denomintor):
            if numerator not in graph or denomintor not in graph: return -1.0
            stack = [[numerator, 1.0]]
            visited = set()
            while stack:
                current, product = stack.pop()
                if current == denomintor: return product
                visited.add(current)
                for neighbour, fraction in graph[current]:
                    if neighbour not in visited: stack.append([neighbour, fraction * product])
            return -1

        for numerator, denomintor in queries:
            res.append(searchGraph(numerator, denomintor))
        return res

        
s = Solution()
print(s.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))