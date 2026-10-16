class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        f = [0, 1, 1]
        while len(f) < 100:
            f.append(f[-1] + f[-2])

        for i in range(2, len(f)):
            if f[i-2] + f[i-1] + f[i] == n:
                return True
                
        return False
        