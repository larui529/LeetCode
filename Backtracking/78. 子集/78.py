"""
78. 子集 - 占位文件
实现位置留空，稍后补充。
"""

from typing import List

# Uniform template: use `res`, `path`, and helper `dfs(start)` across backtracking problems.

def subsets(nums: List[int]) -> List[List[int]]:
    res: List[List[int]] = []
    path: List[int] = []

    def dfs(start: int) -> None:
        # append a copy of current path as one subset
        res.append(path.copy())
        for i in range(start, len(nums)):
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

    dfs(0)
    return res


def subsets_backtrack(nums: List[int]) -> List[List[int]]:
    """Explicit backtracking solution variant (same template).

    Keeps same variable names `res`, `path`, and helper `dfs(start)` so
    you can reuse the pattern across problems.
    """
    res = []
    subset = []
    n = len(nums)

    def backtracking(start):
        if start == n:
            res.append(subset.copy())
            return
        
        
        backtracking(start+1)
        subset.append(nums[start])
        backtracking(start+1)
        subset.pop()

    backtracking(0)
    return res



# keep `subsets` as the canonical name but point to the explicit backtracking
subsets = subsets_backtrack


if __name__ == "__main__":
    print(subsets([1,2,3]))
