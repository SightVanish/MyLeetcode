"""
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.
Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
"""
from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        l = []
        for i in range(len(pushed)):
            l.append(pushed[i])
            while j < len(popped) and l and l[-1] == popped[j]:
                l.pop()
                j += 1
        return len(l) == 0
    

s = Solution()
print(s.validateStackSequences([1,0], [1,0]))



