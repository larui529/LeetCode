"""
39. 组合总和 - 占位文件
实现位置留空，稍后补充。
"""

from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    res: List[List[int]] = []
    path: List[int] = []

    def dfs(start: int, remain: int) -> None:
        if remain == 0:
            res.append(path.copy())
            return
        for i in range(start, len(candidates)):
            c = candidates[i]
            if c > remain:
                break
            path.append(c)
            # allow reuse of the same element => pass i
            dfs(i, remain - c)
            path.pop()

    dfs(0, target)
    return res


if __name__ == "__main__":
    print(combinationSum([2,3,6,7], 7))
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates = sorted(candidates)

        def bk(start, selected, target):
            if target == 0:
                res.append(selected.copy())
                return 
            for i in range(start, n):
                if target < candidates[i]:
                    break
                selected.append(candidates[i])
                bk(i, selected, target - candidates[i])
                selected.pop()
        bk(0, [], target)
        return res