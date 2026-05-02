class Solution:
    def isGood(self, n):
        good = False
        while n > 0:
            digit = n % 10
            if digit == 3 or digit == 4 or digit == 7:
                return False
            elif digit == 2 or digit == 5 or digit == 6 or digit == 9:
                good = True
            n = n // 10
        return good
    def rotatedDigits(self, n: int) -> int:
        cnt = 0
        for i in range(1, n+1):
            if self.isGood(i):
                cnt += 1
        return cnt
        