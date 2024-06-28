class Solution:
    def mySqrt(self, x: int) -> int:
        def find(start, end):
            if start * start > x: return start - 1
            mid = (start + end) // 2
            if mid * mid == x: return mid
            elif mid * mid < x: return find(mid + 1, end)
            else: return find(start, mid - 1)
        return find(1, x)
