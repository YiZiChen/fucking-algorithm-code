class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n_s=len(s)
        dp=[[0]*n_s for i in range(n_s)]
        for i in range(n_s-1,-1,-1):
            dp[i][i]=1
            for j in range(i+1,n_s):
                if s[i]==s[j]:dp[i][j]=dp[i+1][j-1]+2
                else:dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        return dp[0][n_s-1]
