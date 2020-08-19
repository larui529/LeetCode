class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        dp = [[[0]*100 for i in range(100)] for j in range(100)]

        def dfs(boxes, l, r, k):
            if l>r:
                return 0
            
            if dp[l][r][k] != 0:
                return dp[l][r][k]

            while l<r and boxes[r]==boxes[r-1]:
                r -= 1
                k += 1
            
            dp[l][r][k] = dfs(boxes, l, r-1, 0) + (k+1)**2
            
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    dp[l][r][k] = max(dp[l][r][k], dfs(boxes, l, i, k+1) + dfs(boxes, i+1, r-1, 0))
            return dp[l][r][k]
        return dfs(boxes, 0, len(boxes)-1, 0)