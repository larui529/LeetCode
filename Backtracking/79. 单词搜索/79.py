"""
79. 单词搜索 - 占位文件
实现位置留空，稍后补充。
"""

from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    if not board or not board[0]:
        return False
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, i: int) -> bool:
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
            return False
        # mark visited
        tmp = board[r][c]
        board[r][c] = '#'
        found = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )
        board[r][c] = tmp
        return found

    for row in range(rows):
        for col in range(cols):
            if dfs(row, col, 0):
                return True
    return False


if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    print(exist(board, "ABCCED"))
