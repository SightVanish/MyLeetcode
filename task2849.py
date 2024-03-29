"""
You are given four integers sx, sy, fx, fy, and a non-negative integer t.
In an infinite 2D grid, you start at the cell (sx, sy). Each second, you must move to any of its adjacent cells.
Return true if you can reach cell (fx, fy) after exactly t seconds, or false otherwise.
A cell's adjacent cells are the 8 cells around it that share at least one corner with it. You can visit the same cell several times.
"""

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx, dy = abs(fx - sx), abs(fy - sy)
        minimum_t = min(dx, dy) + abs(dx - dy)
        if dx == dy == 0 and t == 1: return False # this is a corner case
        if t >= minimum_t: return True
        return False

s = Solution()
print(s.isReachableAtTime(sx = 1, sy = 2, fx = 1, fy = 2, t = 1))