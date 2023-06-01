"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(min([len(s) for s in strs])):
            if len(set([s[i] for s in strs])) != 1: return strs[0][:i]
        return strs[0][:min([len(s) for s in strs])]


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if strs == []:
            return ""
        pre = strs[0]
        for i in range(1, len(strs)):
            index = 0
            for j in range(0, min(len(pre),len(strs[i]))):
                if pre[j] == strs[i][j]:
                    index += 1
                else:
                    break # if any problem occurs, we need to break instead of continue
            if index == 0:
                return ""
            pre = pre[0:index] # it will return 0<=x<index, index will not be included
        return pre
                
# we can use zip() function for help
# zip:
# a = [1,2,3]
# b = [4,5,6]
# c = [4,5,6,7,8]
# zipped = zip(a,b)     # 打包为元组的列表
# ->[(1, 4), (2, 5), (3, 6)]
# zip(a,c)              # 元素个数与最短的列表一致
# ->[(1, 4), (2, 5), (3, 6)]
# zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
# ->[(1, 2, 3), (4, 5, 6)]


s = Solution()
i = ["aca","cba"]
print(s.longestCommonPrefix(i))
