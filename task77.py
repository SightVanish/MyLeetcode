from typing import List
# my solution
# time/space complexity: O(n^k)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0: return [[]]
        output = [[i] for i in range(1, n+1)]
        for _ in range(k-1):
            output = [o + [m] for o in output for m in range(o[-1]+1, n+1)]
        return output

# backtrack solution
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            if len(curr) == k:
                output.append(curr[:]) # this is a deep copy
                return
            for i in range(first, n + 1):
                curr.append(i)
                backtrack(i + 1, curr) # DFS
                curr.pop() # as this is a shallow copy we need to pop
        output = []
        backtrack()
        return output
s = Solution()
print(s.combine(4,2))