# calculate the fractorial
class Solution:
    def trailingZeroes(self, n: int) -> int:
        val, count = 1, 0
        for i in range(n): val *= (i + 1)
        while val % 10 == 0:
            count += 1
            val = val // 10
        return count

# 0 can only be created via 2*5, n! can be denoted as 2^a * 3^b * 5^c * ....
# thus number of 0 = min(number of 2, number of 5)
# as the number of 2 must be smaller than 5, we only need to count the number of 5
class Solution:
    def trailingZeroes(self, n: int) -> int:
        val = 5
        count = 0
        # count how many integers contain 5, 25, 125, etc
        while val <= n:
            count += n // val
            val *= 5
        return count

s = Solution()
print(s.trailingZeroes(100))