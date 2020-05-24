class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        dp = [[0]*(steps//2+2) for i in range(steps+1)] 
        dp[0][0] = 1
        mod = 10**9+7
        for i in range(1, steps+1):
            for j in range(steps//2+1): # position
                if j==0:
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j+1])%mod
                elif j==arrLen-1:
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j-1])%mod
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j+1] + dp[i-1][j-1])%mod
        
        return dp[-1][0]

                

        
        # dp[i][j]: i step at position j