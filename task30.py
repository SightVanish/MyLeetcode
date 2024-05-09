from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def check(d1, d2):
            # 0: all good, 1: short, 2: more
            d = 0
            for k in d1.keys():
                if d1[k] > d2[k]: return 2
                elif d1[k] < d2[k]: d = 1
            return d
        targets, count = {}, {}
        for w in words:
            if w in targets: targets[w] += 1
            else: targets[w] = 1
            count[w] = 0
        n = len(words[0])
        res = []
        for start_index in range(n): # try each starting point
            i, j = start_index, start_index
            for w in count.keys(): count[w] = 0
            while j < len(s):
                c = check(count, targets)
                if c == 0: 
                    res.append(i)
                    count[s[i:i+n]] -= 1
                    i += n
                elif c == 1:
                    if s[j:j+n] not in words:
                        i, j = j + n, j + n
                        for w in count.keys(): count[w] = 0
                    else:
                        count[s[j:j+n]] += 1
                        j += n
                elif c == 2:
                    count[s[i:i+n]] -= 1
                    i += n
            if check(count, targets) == 0: res.append(i)
        return res
s = Solution()
print(s.findSubstring("wordgoodgoodgoodbestword", words = ["word","good","best","good"]))
