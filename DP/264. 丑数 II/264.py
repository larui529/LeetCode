class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n+1)]
        a, b, c = 1, 1, 1
        dp[1] = 1
        min_can = float('inf')

        for i in range(2, n+1):
            can1 = dp[a]*2
            can2 = dp[b]*3
            can3 = dp[c]*5
            min_can = min(can1, can2, can3)
            if can1==min_can:
                a+=1
            if can2==min_can:
                b+=1
            if can3==min_can:
                c+=1
            dp[i] = min_can
            # print (can1, can2, can3, min_can)
        return dp[n]

