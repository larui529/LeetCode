"""
46. 全排列 - 占位文件
实现位置留空，稍后补充。
"""

from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    res: List[List[int]] = []
    path: List[int] = []
    used = [False] * len(nums)

    def dfs() -> None:
        if len(path) == len(nums):
            res.append(path.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            dfs()
            path.pop()
            used[i] = False

    dfs()
    return res


if __name__ == "__main__":
    print(permute([1,2,3]))
