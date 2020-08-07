class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        lookup = {}

        def add(word, tree):
            for e in word:
                if e not in tree:
                    tree[e] = {}
                tree = tree[e]
            tree['#'] = {}
        
        for word in words:
            add(word, lookup)
        res = []
        # print (lookup)
        m, n = len(board), len(board[0])
        def dfs(board, visited, i, j, tree, chosen):
            if i<0 or j<0 or i>=m or j>=n or visited[i][j]==1:
                return 
            # print (i, j, board[i][j],chosen)
            # if '#' in tree:
            #     res.append(chosen[:])
                
            if board[i][j] in tree:
                visited[i][j] = 1
                chosen.append(board[i][j])
                if '#' in tree[board[i][j]]:
                    res.append(chosen[:])
                
                dirs = [[0,1],[0,-1],[1,0],[-1,0]]
                for d in dirs:
                    x, y = i+d[0], j+d[1]
                    dfs(board, visited, x, y, tree[board[i][j]], chosen)
                visited[i][j] = 0
                chosen.pop()
            return 
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in lookup:
                    visited = [[0]*n for k in range(m)]
                    dfs(board, visited, i, j, lookup, [])
        l = len(res)
        for i in range(l):
            res[i] = ''.join(res[i])
        
        return list(set(res))


            