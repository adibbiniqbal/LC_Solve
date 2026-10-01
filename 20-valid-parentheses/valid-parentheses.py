class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif len(stack) > 0 and c == ')' and stack[-1] == '(':
                stack.pop()
            elif len(stack) > 0 and c == '}' and stack[-1] == '{':
                stack.pop()
            elif len(stack) > 0 and c == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
        