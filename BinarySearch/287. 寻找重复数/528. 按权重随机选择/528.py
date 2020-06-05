class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.nums = []
        self.agg = 0
        for num in w:
            self.agg += num
            self.nums.append(self.agg)

    def pickIndex(self):
        """
        :rtype: int
        """
        from random import randint
        import bisect
        randNum = randint(1, self.agg)
        index = bisect.bisect_left(self.nums, randNum)
        return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()