class Solution(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        text = "#"+text
        n = len(text)
        dp = [[0]*n for i in range(n)]
        visited = set()
        
        for i in range(1, n):
            for j in range(i+1, n):
                if text[i]==text[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                if dp[i][j]>=j-i:
                    visited.add(text[i+1:j+1])         
        
        return len(visited)




        