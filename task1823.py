# time: O(n), space: O(n)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n <= 1: return n
        queue = [i + 1 for i in range(n)]
        i = 0
        while len(queue) > 1:
            i = (k % len(queue) - 1 + i) % len(queue)
            del queue[i]
        return queue[0]

# Josephus problem approach, time: O(n), space: O(n)
# base case: J(1, k) = 0 -- 0-index
# J(n, k) = (J(n-1, k)+k)%n
# new_position=(previous_position+k−1)%n+1 -- 1-index, why (xxx-1)%n? because % is 0-based operator
# for J(n, k): 1,2,3...,n -> remove k -> 1,2,3,...k-1,k+1,...n -> k+1,...n,1,2,3,...k-1 -> J(n-1, k) but start at k+1 instead of 1 

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1: return 1
        else: return (self.findTheWinner(n - 1, k) - 1 + k) % n + 1
# write in O(1) space complexity
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        pos = 1
        for i in range(1, n): pos = (pos - 1 + k) % (i + 1) + 1
        return pos

s = Solution()
print(s.findTheWinner(n = 5, k = 2))