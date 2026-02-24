from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]
        elif s < target:
            l += 1
        else:
            r -= 1
    return []


if __name__ == '__main__':
    print(twoSum([2,7,11,15], 9))

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n-1
        res = []
        total = 0
        while l < r:
            total = numbers[l] + numbers[r]
            # print(l, r, total)
            if total == target:
                return [l+1, r+1]
            if total > target: 
                r -= 1
            else:
                l += 1
        