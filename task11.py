# try dynamic programming--it takes too much time 
# class Solution:
#     def maxArea(self, height) -> int:
#         # dynamic programing
#         result = [[0 for _ in range(len(height))] for _ in range(len(height))]
#         for i in range(0, len(height)):
#             for j in range(i, len(height)):
#                 if(i == j):
#                     result[i][j] = 0 # init
#                 elif (j - i) == 1:
#                     result[i][j] = min(height[i], height[j]) # init
#                 else:
#                     continue
#         for i in range(0, len(height)):
#             for j in range(i, len(height)):
#                 if i > 0:
#                     result[i][j] = max(max(result[i-1][j],result[i][j-1]),(j-i)*min(height[i],height[j]))
#                 else:
#                     result[i][j] = max(result[i][j-1],(j-i)*min(height[i],height[j]))
#         print(result)
#         return result[len(height)-1][len(height)-1]

# try to use 2 pointer
class Solution:
    def maxArea(self, height) -> int:
        head, tail = 0, len(height)-1
        result = (tail-head)*min(height[head],height[tail])
        while(head < tail):
            if height[head] < height[tail]:
                head += 1
            else:
                tail -= 1
            result = max(result, (tail-head)*min(height[tail],height[head]))
        return result

s = Solution()
h = [1,2,3,4]
print(s.maxArea(h))
