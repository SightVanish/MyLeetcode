from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, line, count = [], [], 0
        for w in words:
            if count + len(line) + len(w) > maxWidth: 
                # add space from left to right, 'or 1' for case when line contains only one element
                for i in range(maxWidth-count): line[i%(len(line)-1 or 1)] += ' ' 
                res.append(''.join(line))
                line, count = [], 0
            count += len(w)
            line.append(w)
        res.append(' '.join(line).ljust(maxWidth))
        return res
s = Solution()
print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
        
