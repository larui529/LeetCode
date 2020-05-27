class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        n = len(s)
        num = ''
        for i in range(n):
            if s[i].isnumeric():
                num+=s[i]
            elif s[i].isalpha():
                stack.append(s[i])
            elif s[i] == '[':
                stack.append(int(num))
                num = ''
            elif s[i] == ']':
                tmp_str = ''
                while type(stack[-1])!=int:
                    tmp_str = stack.pop() + tmp_str
                tmp_str = tmp_str*stack.pop()
                stack.append(tmp_str)
            # print (stack)
        return ''.join(stack)
