from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        dic = {} # the end index of this char
        for index, char in enumerate(s):
            dic[char] = index
        start = 0
        while (start < len(s)):
            end = dic[s[start]]
            p = start
            while p < end:
                if dic[s[p]] > end:
                    end = dic[s[p]]
                p += 1     
            result.append(end-start+1)
            start = end + 1
        return result
    
s = Solution()
test = "ababcbacadefegdehijhklij"
print(s.partitionLabels(test))