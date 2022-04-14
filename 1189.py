# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         self.ballon = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
#         for c in text:
#             if c in self.ballon:
#                 self.ballon[c] += 1
#         self.ballon['l'] /= 2
#         self.ballon['o'] /= 2

#         return int(min(self.ballon.values))
        
            
text = "leetcode"
ballon = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
for c in text:
    if c in ballon:
        ballon[c] += 1
ballon['l'] /= 2
ballon['o'] /= 2

print(int(min(ballon.values())))