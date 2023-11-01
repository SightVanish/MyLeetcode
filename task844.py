"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
"""
 
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s), len(t)
        def get_next_valid_char(s, index):
            num_backspace = 0
            while index >= 0:
                if s[index] == '#': num_backspace += 1
                else:
                    if num_backspace > 0: num_backspace -= 1
                    else: break
                index -= 1
            return index
        while i >= 0 and j >= 0:
            i, j = get_next_valid_char(s, i-1), get_next_valid_char(t, j-1)
            if i == j == -1: return True
            if s[i] != t[j]: return False
        if i == j: return True
        return False

s = Solution()
print(s.backspaceCompare(s = "ab#cc#", t = "ad#c"))