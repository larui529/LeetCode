class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 1 2 3 3 3 4 5  [1,6] 
        # k = 4

        n = len(nums)-1

        def dupNumLessOrEqual(k):
            cnt = 0
            for i in range(len(nums)):
                if nums[i]<=k:
                    cnt+=1
            return cnt>k
            

        left, right = 1, n
        while left<right:
            mid = left+(right-left)//2
            if dupNumLessOrEqual(mid):
                right = mid
            else:
                left = mid+1
        return left

       