class Solution:
    def calculate(self, s: str) -> int:
        results, operators = [], []
        res, number, operator = 0, 0, 1
        for i in s:
            if i.isdigit():
                number = number * 10 + int(i) # current number
            elif i in '+-':
                res += operator * number
                operator = 1 if i == '+' else -1
                number = 0
            elif i == '(':
                results.append(res)
                operators.append(operator)
                res, number, operator = 0, 0, 1
            elif i == ')':
                res += operator * number
                number, operator = results.pop(), operators.pop()
                res = number + operator * res
                number, operator = 0, 1
        return res + number * operator

s = Solution()
print(s.calculate('1+1'))