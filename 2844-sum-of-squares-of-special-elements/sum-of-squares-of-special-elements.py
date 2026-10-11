class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        length = len(nums)
        ans = 0
        for i in range(length):
            if length % (i + 1) == 0:
                ans += nums[i] * nums[i]
        return ans
