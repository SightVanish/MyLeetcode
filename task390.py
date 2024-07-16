# the last number that remains if we start from left to right then right to left is: f(n)
# the last number that remains if we start from right to left then left to right is: f'(n)
# f(n) and f'(n) must have symmetric position which means: f(n) + f'(n) == n + 1
# f(n) = 2 * (f'(n // 2))
class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1: return 1
        else: return 2 * (n // 2 + 1 - self.lastRemaining(n // 2))
s = Solution()
print(s.lastRemaining(9))
