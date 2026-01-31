# 79. 单词搜索

问题描述（简述）：给定一个 m x n 的字符网格 board 和一个字符串 word，判断 word 是否存在于网格中。单词必须由顺邻（上下左右）相邻的单元格构成，同一个单元格不能被重复使用。

解题思路（中文）：
- 回溯（DFS）+ 回溯标记：遍历每个起点，深度优先搜索匹配字符序列，使用访问标记避免重复使用同一格子。若某路径匹配失败则回溯，把格子标记复原。
- 剪枝：若当前字符不匹配或超过边界则剪枝；尽早返回以减少搜索。

复杂度提示：在最坏情况下，时间复杂度为 O(m*n*4^L)，其中 L 是单词长度。

English (paraphrased): Given an m x n board of characters and a word, return true if the word exists in the grid. The word must be constructed from sequentially adjacent cells (horizontally or vertically), and the same cell cannot be used more than once.

Example:
Input:
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
Output: true

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15

Solution idea: Use DFS with `dfs(r,c,i)` where `i` is current index in `word`. Use `res` not needed; return True when found. Keep `path` naming for uniform parts where applicable and use in-place marking or `visited`.
