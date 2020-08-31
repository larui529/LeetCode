class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        count = 0
        max_remove = 0
        for i in range(n):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
            if count <0:
                max_remove += 1
                count = 0
        res_len = n - max_remove
        res = []
        dfs(s, index, cur_s, count):
            if count < 0:
                return
            if index == n:
                if len(cur_s) == res_len and count == 0:
                    res.append(cur_s)
                return

            if s[i] not in ['(', ')']:
                dfs(s, index+1, cur_s+s[index], count)
                return
            dfs(s, index+1, cur_s+s[index], count + (1 if s[index]=='(' else -1))
            if s[index]!=cur_s[-1]:
                dfs(s, index+1, cur_s, count)

            return
        dfs(s, 0, '', 0)
        return res
