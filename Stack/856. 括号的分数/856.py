class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        k = 0
        stack = []
        for i in range(n):
            if S[i]=='(':
                k+=1
            else:
                k-=1
                val, layer = 0, k
                if S[i-1]=='(':
                    val = 1
                else:
                    val, _ = stack.pop()
                    val*=2
                while stack and stack[-1][1]==layer:
                    val2 = stack.pop()[0]
                    val += val2
                stack.append([val, layer])
        return stack[-1][0]
       
        # (()()()((()(((())))((()()())))))
        # ( ( ( ) ) ( ( ( ) ) ) ( ( ) ) )
        # 1 2 3 2 1 2 3 4 3 2 1 2 3 2 1 0
        # 0 1 2 3 4 5 6 7 8 9 101112131415
            
        # if S[i] == ')' and S[i-1] == '(':
        #     stack.append([1, k])
        # else:
        #     val, layer = stack.pop()
        #     val*=2
        #     layer-=1
        #     while stack and stack[-1][1]==layer:
        #         val2 = stack.pop()[0]
        #         val += val2
        #     stack.append([val, layer])

        # i = 3 => [[1,2]]
        #     4 => [[2,1]]
        #     8 => [[2,1][1,3]]
        #     9 => [[2,1][2,2]]
        #     10 =>[[5,1]]
        #     13 =>[[5,1],[1,2]]
        #     14 =>[[7,1]]
        #     15 =>[[14,0]]
        