class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[-1<<31]
        length_nums=len(nums)
        for i in range(length_nums):
            dp.append(max(nums[i],dp[i]+nums[i]))
        return max(dp)
