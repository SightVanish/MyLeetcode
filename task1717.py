class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        stack = ['', '']
        i = 0
        while i < len(s):
            stack.append(s[i])
            # aba or bab
            if i < len(s) - 1 and ((s[i + 1] == 'a' and stack[-1] == 'b' and stack[-2] == 'a') or (s[i + 1] == 'b' and stack[-1] == 'a' and stack[-2] == 'b')):
                i += 1
                stack.append(s[i])
            while (stack[-1] == 'b' and stack[-2] == 'a') or (stack[-1] == 'a' and stack[-2] == 'b'):
                if (stack[-1] == 'a' and stack[-2] == 'b' and stack[-3] == 'a') or (stack[-1] == 'b' and stack[-2] == 'a' and stack[-3] == 'b'): res += max(x, y)
                elif stack[-1] == 'b' and stack[-2] == 'a': res += x
                elif stack[-1] == 'a' and stack[-2] == 'b': res += y
                del stack[-2:]
            i += 1
        return res
s = Solution()
print(s.maximumGain("aabbaaxybbaabb", 5, 4))