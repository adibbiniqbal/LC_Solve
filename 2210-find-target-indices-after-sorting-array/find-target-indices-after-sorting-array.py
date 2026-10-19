class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        ans = [i for i, n in enumerate(nums) if n == target]
        return ans
        