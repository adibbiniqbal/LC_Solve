class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        i, N, ans = 0, len(nums), 0
        while i < N:
            if i + 1 < N and nums[i] == nums[i+1]:
                ans += 1
            i += 1
        return ans 

        