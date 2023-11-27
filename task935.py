"""
The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:
A chess knight can move as indicated in the chess diagram below:
"""

class Solution:
    def knightDialer(self, n: int) -> int:
        res = 0
        status = [[-1 for _ in range(10)] for _ in range(n+1)]

        def numCombinations(position, length):
            if length == 0: return 1
            if status[length][position] == -1:
                if position == 0: status[length][position] = numCombinations(4, length-1) + numCombinations(6, length-1)
                elif position == 1: status[length][position] = numCombinations(6, length-1) + numCombinations(8, length-1)
                elif position == 2: status[length][position] = numCombinations(7, length-1) + numCombinations(9, length-1)
                elif position == 3: status[length][position] = numCombinations(4, length-1) + numCombinations(8, length-1)
                elif position == 4: status[length][position] = numCombinations(0, length-1) + numCombinations(3, length-1) + numCombinations(9, length-1)
                elif position == 5: status[length][position] = 0
                elif position == 6: status[length][position] = numCombinations(0, length-1) + numCombinations(1, length-1) + numCombinations(7, length-1)
                elif position == 7: status[length][position] = numCombinations(2, length-1) + numCombinations(6, length-1)
                elif position == 8: status[length][position] = numCombinations(1, length-1) + numCombinations(3, length-1)
                elif position == 9: status[length][position] = numCombinations(2, length-1) + numCombinations(4, length-1)
            return status[length][position]

        for i in range(10): res += numCombinations(i, n-1)
        return res % (10**9 + 7)

s = Solution()
print(s.knightDialer(2))
      