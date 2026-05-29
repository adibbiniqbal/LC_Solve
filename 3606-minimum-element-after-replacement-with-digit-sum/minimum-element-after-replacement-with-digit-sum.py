class Solution:
    def minElement(self, nums: List[int]) -> int:
        minDigit = float('inf')
        for num in nums:
            digitSum = sum(map(int, str(num)))
            minDigit = min(minDigit, digitSum)
        return minDigit