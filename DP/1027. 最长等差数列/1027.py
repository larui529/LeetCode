class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        from collections import defaultdict
        n = len(A)
        dp = [defaultdict(int) for i in range(n)]
        res = 0

        for i in range(1, n):
            for j in range(i-1, -1, -1):
                diff = A[i]-A[j]
                
                if diff not in dp[j]:
                    dp[j][diff] = 1
                dp[i][diff] = max(dp[i][diff], dp[j][diff]+1) 
                    
                res = max(res, dp[i][diff])     
        return res
