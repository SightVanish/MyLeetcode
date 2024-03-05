class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s) - 1
        while i < j and s[i] == s[j]:
            t = s[i]
            while i <= j and s[i] == t: i += 1
            while i <= j and s[j] == t: j -= 1
        return j - i + 1

s = Solution()
print(s.minimumLength("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"))
        
