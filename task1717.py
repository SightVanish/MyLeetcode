class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        if x > y: prefix = ['ab', 'ba']
        else: 
            prefix = ['ba', 'ab']
            x, y = y, x

        for p in prefix:
            stack = ['', '']
            for w in s:
                stack.append(w)
                while stack and stack[-2] + stack[-1] == p:
                    res += x
                    del stack[-2:]
            x = y
            s = ''.join(stack)
        return res


s = Solution()
print(s.maximumGain("aabbaaxybbaabb", 5, 4))

# aaxybbaab