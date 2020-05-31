class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length_word1=len(word1)
        length_word2=len(word2)
        dp=[[0]*(length_word2+1) for i in range(length_word1+1)]
        for i in range(length_word1+1):
            dp[i][0]=i
        for i in range(length_word2+1):
            dp[0][i]=i
        for i in range(1,length_word1+1):
            for j in range(1,length_word2+1):
                if word2[j-1]==word1[i-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j-1]+1,dp[i-1][j]+1,dp[i][j-1]+1)
        return dp[length_word1][length_word2]
