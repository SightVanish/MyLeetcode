"""
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.
"""

# class Solution:
#     def countVowelPermutation(self, n: int) -> int:
#         num = [[-1 for _ in range(5)] for _ in range(n)] # num[n][0] starts for 'a', same for 'e', 'i', 'o', 'u'
#         num[0] = [1] * 5

#         def count(i, end):
#             if num[i][end] != -1: return num[i][end]
#             elif end == 0: num[i][end] = count(i-1, 1) + count(i-1, 4) + count(i-1, 2) # a
#             elif end == 1: num[i][end] = count(i-1, 0) + count(i-1, 2) # e
#             elif end == 2: num[i][end] = count(i-1, 1) + count(i-1, 3) # i
#             elif end == 3: num[i][end] = count(i-1, 2) # o
#             elif end == 4: num[i][end] = count(i-1, 3) + count(i-1, 2) # u
#             return num[i][end]
#         # print(count(n-1, 0),count(n-1, 1),count(n-1, 2),count(n-1, 3),count(n-1, 4))
#         res = count(n-1, 0) + count(n-1, 1) + count(n-1, 2) + count(n-1, 3) + count(n-1, 4)
        
#         return res % (10**9 + 7)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1 # num of possible sequence ending with 'a', 'e', etc.
        for _ in range(n-1):
            a_next = e + u + i
            e_next = a + i
            i_next = e + o
            o_next = i
            u_next = o + i
            a, e, i, o, u = a_next, e_next, i_next, o_next, u_next
        return (a + e + i + o + u) % (10**9 + 7)


s = Solution()
print(s.countVowelPermutation(144))
        