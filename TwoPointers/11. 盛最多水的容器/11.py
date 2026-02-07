from typing import List

def maxArea(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    ans = 0
    while l < r:
        h = min(height[l], height[r])
        ans = max(ans, h * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return ans


if __name__ == '__main__':
    print(maxArea([1,8,6,2,5,4,8,3,7]))


class Solution:
    def maxArea(self, H: List[int]) -> int:
        n = len(H)
        l, r = 0, n-1
        max_area = 0

        while l < r:
            area = (r-l) * min(H[l], H[r])
            max_area = max(area, max_area)
            # print(l, r, area)
            if H[l] >= H[r]:
                r -= 1
            else:
                l += 1
        
        return max_area