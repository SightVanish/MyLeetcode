class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ')': stack.append(i)
            else:
                reverse = []
                p = stack.pop()
                while p != '(':
                    reverse.append(p) # already reverse
                    p = stack.pop()
                stack.extend(reverse)
        return ''.join(stack)

        

s = Solution()
print(s.reverseParentheses("ta()usw((((a))))"))