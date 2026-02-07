from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    res: List[List[int]] = []
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        l, r = i + 1, n - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif s < target:
                l += 1
            else:
                r -= 1
    return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i+1, n-1
            while j<k:
                # print (nums[i], nums[j], nums[k])
                ijk_sum = nums[i] + nums[j] + nums[k]
                if ijk_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    while j<k and nums[k] == nums[k+1]:
                        k -= 1
                elif ijk_sum < 0:
                    j += 1
                else:
                    k -= 1
        return res

if __name__ == '__main__':
    print(threeSum([-1,0,1,2,-1,-4]))
