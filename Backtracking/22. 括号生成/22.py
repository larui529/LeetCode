"""
22. 括号生成 - 占位文件
实现位置留空，稍后补充。
"""

from typing import List

def generateParenthesis(n: int) -> List[str]:
    res: List[str] = []

    def dfs(left: int, right: int, path: List[str]) -> None:
        if left == n and right == n:
            res.append(''.join(path))
            return
        if left < n:
            path.append('(')
            dfs(left + 1, right, path)
            path.pop()
        if right < left:
            path.append(')')
            dfs(left, right + 1, path)
            path.pop()

    dfs(0, 0, [])
    return res


if __name__ == "__main__":
    print(generateParenthesis(3))
