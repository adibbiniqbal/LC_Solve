class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        count, score = 0, 0
        for i, c in enumerate(s):
            if c == '(':
                count += 1
            else:
                count -= 1
                if s[i-1] == '(':
                    score += 1 << count
        return score