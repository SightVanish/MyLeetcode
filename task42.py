class Solution:        
    def trap(self, height: list[int]) -> int:
        # height from left to right
        leftRightHeight = [0 for _ in range(len(height))]
        max_height = 0
        for i in range(0, len(height)):
            max_height = max(max_height, height[i])
            leftRightHeight[i] = max_height
        # height from right to left
        rightLeftHeight = [0 for _ in range(len(height))]
        max_height = 0
        for i in range(len(height) - 1, -1, -1):
            max_height = max(max_height, height[i])
            rightLeftHeight[i] = max_height

        volumn = [min(leftRightHeight[i], rightLeftHeight[i]) - height[i] for i in range(len(leftRightHeight))]

        return sum(volumn)

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))