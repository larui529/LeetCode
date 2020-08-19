class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        sold1 = [0 for i in range(n+1)]
        sold2 = [0 for i in range(n+1)]
        hold1 = [0 for i in range(n+1)]
        hold2 = [0 for i in range(n+1)]
        hold1[0], hold2[0] = -float('inf'), -float('inf')

        for i in range(1, n+1):

            sold1[i] = max(sold1[i-1], hold1[i-1]+prices[i-1])
            sold2[i] = max(sold2[i-1], hold2[i-1]+prices[i-1])
            hold1[i] = max(0-prices[i-1], hold1[i-1])
            hold2[i] = max(sold1[i-1]-prices[i-1], hold2[i-1])

        return max(sold1[n], sold2[n])