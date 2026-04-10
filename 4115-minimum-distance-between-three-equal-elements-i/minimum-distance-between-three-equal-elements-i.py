class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        sum, ans = 0, 2 ** 31
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] == nums[j] and nums[j] == nums[k]:
                        sum = 2 * (k - i)
                        # j - i + k - i + k - j = 2 * (k - i)
                        ans = min(sum, ans)
        return ans if ans != 2 ** 31 else - 1