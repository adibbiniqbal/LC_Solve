class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left_rem, right_rem = 0, 0
        for c in s:
            if c == '(':
                left_rem += 1
            elif c == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1
        
        res = set()
        def recurse(idx, left_cnt, right_cnt, left_rem, right_rem, expr):
            if idx == len(s):
                if left_rem == 0 and right_rem == 0:
                    res.add(expr)
                return

            char = s[idx]

            if char != '(' and char != ')':
                recurse(idx + 1, left_cnt, right_cnt, left_rem, right_rem, expr + char)

            if char == '(' and left_rem > 0:
                recurse(idx + 1, left_cnt, right_cnt, left_rem - 1, right_rem, expr)
            elif char == ')' and right_rem > 0:
                recurse(idx + 1, left_cnt, right_cnt, left_rem , right_rem - 1, expr)

            if char == '(':
                recurse(idx + 1, left_cnt + 1, right_cnt, left_rem, right_rem, expr + char)
            elif char == ')' and left_cnt > right_cnt:
                recurse(idx + 1, left_cnt, right_cnt + 1, left_rem, right_rem, expr + char)

        recurse(0, 0, 0, left_rem, right_rem, "")
        return list(res)