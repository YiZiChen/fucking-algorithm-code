class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_num=sum(nums)
        half_sum_num = sum_num/2
        if half_sum_num!=int(half_sum_num):
            return False
        dp=[False]*int(half_sum_num+1)
        dp[0]=True
        for i in nums:
            for j in range(int(half_sum_num),i-1,-1):
                dp[j]=dp[j] or dp[j-i]
        return dp[-1]
