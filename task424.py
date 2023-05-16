"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {} # record frequency of each distinct letter
        # in subarray s[l:r], we only convert all letters to the most frequent letter 
        l, r, res, maxFrequency = 0, 0, 0, 0
        while r < len(s):

            counter[s[r]] = 1 + counter.get(s[r], 0) # update frequcey
            maxFrequency = max(counter.values())
            # if we cannot replace all letters that are not same with the most frequent letter, we move left index
            if r - l + 1 - maxFrequency > k:
                counter[s[l]] -= 1
                l += 1
                r += 1
            else:
                res = max(res, r - l + 1)
                r += 1    
        return res
    

s = Solution()
print(s.characterReplacement("AABABBA", 1))
