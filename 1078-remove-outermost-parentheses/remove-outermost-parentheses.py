class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        bal = 0
        for c in s:
            if c == '(':
                bal += 1
                if bal > 1:
                    result += c
            else:
                bal -= 1
                if bal > 0:
                    result += c
        return result
        