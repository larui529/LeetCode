class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        dp = [[[-float('inf')]*n for i in range(n)] for j in range(m)]
        dp[0][0][n-1] = grid[0][0] + grid[0][n-1]
        moves = [-1,0,1]

        for i in range(m-1):
            for j in range(n):
                for k in range(n):
                    for jj in moves:
                        for kk in moves:
                            if j+jj<0 or j+jj>=n or k+kk<0 or k+kk>=n or j+jj==k+kk or dp[i][j][k]==-float('inf'):
                                continue
                            dp[i+1][j+jj][k+kk] = max( dp[i+1][j+jj][k+kk], dp[i][j][k] + grid[i+1][j+jj]+grid[i+1][k+kk])
        
        res = 0
        for j in range(n):
            for k in range(n):
                res = max(res, dp[-1][j][k])
        return res


       