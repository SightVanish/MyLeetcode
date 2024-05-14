from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for i in tokens:
            if i not in ('+', '-', '*', '/'): numbers.append(int(i))
            else:
                n1 = numbers.pop()
                n2 = numbers.pop()
                if i == '+': numbers.append(n1 + n2)
                elif i == '-': numbers.append(n2 - n1)
                elif i == '*': numbers.append(n1 * n2)
                elif i == '/': numbers.append(int(n2 / n1))
        return numbers[0]
s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))