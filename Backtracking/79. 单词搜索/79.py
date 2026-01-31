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

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        l = len(word)
        
        def bk(x, y, index):
            # print(board,x,y, index)
            if index == l:
                return True
            
            if x<0 or y<0 or x>=m or y>=n or board[x][y] != word[index]:
                return False
            
            temp = board[x][y]
            board[x][y] = "#"
            for i, j in [(0,1), (1,0), (-1,0), (0,-1)]:
                new_x, new_y = x+i, y+j
                if bk(new_x, new_y, index+1):
                    return True
            board[x][y] = temp
        
        for a in range(m):
            for b in range(n):
                if bk(a, b, 0):
                    return True
        return False

