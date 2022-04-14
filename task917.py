class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i, j = 0, len(s)-1
        s = list(s)
        while(i < j):
            if not s[i].isalpha():
                i += 1
            elif not s[j].isalpha():
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            
        s = ''.join(s)
        return s

ans = Solution()
s = "Test1ng-Leet=code-Q!"
print(ans.reverseOnlyLetters(s))
