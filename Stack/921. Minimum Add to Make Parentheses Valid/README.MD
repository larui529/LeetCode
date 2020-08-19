Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

Example 1:

Input: "())"
Output: 1
Example 2:

Input: "((("
Output: 3
Example 3:

Input: "()"
Output: 0


这道题和某一周的周赛题类似，都是用counter 来解决括号问题。

首先确定可能遇到的情况，定义一个balance表示之前累积的左右括号平衡情况，正表示左括号多，负表示右括号多，如果balance>=0 and '('. 表明可以在后边用右括号进行补救，不需要进行操作，只要在balance+1即可。

如果balance<0 and '(' 说明无法在后边进行补救，那么现在必须在前边加左括号进行补救，补多少有blanace决定，补完后记得balance要重新设置为1

如果balance>=0 and ')' 和balance < 0 and ')'，这两种情况要不就是可以在后边加右括号进行补救，或者正在进行补救，这事都不需要在前边加括号，可以先观望然后再决定是否要再前边加括号。

最后不上balance绝对值的相反括号就可。