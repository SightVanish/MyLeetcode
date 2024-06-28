class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        sign = 0 if n < 0 else 1
        n = abs(n)
        exp, res = 1, x
        while exp * 2 <= n:
            res *= res
            exp *= 2
        for _ in range(n-exp):
            res *= x
        return res if sign else 1.0/res

class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = 0 if n < 0 else 1
        n = abs(n)
        def calculate(x, n):
            if n == 0: return 1
            if n % 2: return x * calculate(x * x, n // 2)
            else: return calculate(x * x, n // 2)
        return calculate(x, n) if sign else 1 / calculate(x, n)

s = Solution()
print(s.myPow(2, 10))