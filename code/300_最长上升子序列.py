class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        len_n=len(nums)
        if len_n==0:return 0
        length_nums=[]
        for i in range(len_n):
            max_length=1
            for j in range(i):
                max_length=max(max_length,length_nums[j]+1 if nums[j]<nums[i] else 0)
            length_nums.append(max_length)
        return max(length_nums)