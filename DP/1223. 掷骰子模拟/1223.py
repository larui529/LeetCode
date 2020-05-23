class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        mod = 10**9+7

        m = max(rollMax)
        dp = [[[0]*(m+1) for i in range(6)] for j in range(n+1)] 
        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n+1): # i th time to roll
            for j in range(6): # j'th number
                for k in range(1, min(rollMax[j]+1, n+1)): # k th continuous number
                    if k>1:
                        dp[i][j][k] = dp[i-1][j][k-1]
                    else:
                        for jj in range(6):
                            for kk in range(1, min(rollMax[jj]+1, n+1)):
                                if jj!=j:
                                    dp[i][j][k] += dp[i-1][jj][kk]
                                    dp[i][j][k]%=mod
        res = 0
        for j in range(6):
            for k in range(1, min(rollMax[j]+1, n+1)):
                res += dp[-1][j][k]
                res%=mod
        return res

        # dp[i][j][k]: 在i次投出j（0indexed）连续k次可以有的最大组合
        # 如果k>1, 说明上一次投出的也是j，那么dp[i][j][k] = dp[i-1][j][k-1]
        # 如果k==1，说明第一次投出j，那么dp[i][j][k]就等于上一次不投出j的所有组合之和