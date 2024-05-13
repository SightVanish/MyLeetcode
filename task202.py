class Solution:
    def isHappy(self, n: int) -> bool:
        history = set()
        while n not in history and n != 1:
            history.add(n)
            n = sum([int(i)**2 for i in list(str(n))])
        if n == 1: return True
        return False
s = Solution()
print(s.isHappy(19))