class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        res = 0
        balance = 0
        n = len(S)
        
        for i in range(n):
            if S[i] == '(' and balance >=0:
                balance += 1
            elif S[i] == ')' and balance >= 0:
                balance -= 1
            elif S[i] == ')' and balance < 0:
                balance -= 1
            elif S[i] == '(' and balance <0:
                res += abs(balance)
                balance = 1
            # print (balance)
        res += abs(balance)
        
        return res