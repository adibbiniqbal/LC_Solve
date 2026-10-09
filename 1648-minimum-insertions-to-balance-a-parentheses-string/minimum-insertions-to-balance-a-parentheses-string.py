class Solution:
    def minInsertions(self, s: str) -> int:
        insersions, leftCnt, idx, length = 0, 0, 0, len(s)
        while idx < length:
            if s[idx] == "(":
                leftCnt += 1
                idx += 1
            else:
                if leftCnt > 0:
                    leftCnt -= 1
                else:
                    insersions += 1
                if idx < length - 1 and s[idx+1] == ")":
                    idx += 2
                else:
                    insersions += 1
                    idx += 1
        insersions += leftCnt * 2
        return insersions
