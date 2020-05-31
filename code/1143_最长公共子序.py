class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n_1=len(text1)
        n_2=len(text2)
        dp=[[0]*(n_1+1) for i in range(n_2+1)]
        for i in range(1,n_2+1):
            for j in range(1,n_1+1):
                if text1[j-1]==text2[i-1]:dp[i][j]=dp[i-1][j-1]+1
                else:dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[n_2][n_1]

