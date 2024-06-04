from typing import List
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        n = len(startGene)
        mutation = 'ACGT'
        visited = set()
        queue = deque()
        queue.append((startGene, 0))
        while queue:
            curr, step = queue.popleft()
            if curr == endGene: return step
            visited.add(curr)
            for i in range(n):
                for m in mutation:
                    new_gene = curr[:i] + m + curr[i+1:]
                    if new_gene not in visited and new_gene in bank: queue.append((new_gene, step + 1))
        return -1

s = Solution()
print(s.minMutation("AACCGGTT", "AACCGGTA", []))
