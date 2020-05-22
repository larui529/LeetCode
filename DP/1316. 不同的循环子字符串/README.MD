这个题如果用暴力的解法遍历所有的substring然后按sub1==sub2这种形式来查看是否有echo的话时间复杂度太大，是O(N3)，会TLE，所以我们要用dp来验证echo string

具体思路就是用一个二维dp[i][j]来表示从头到以i和j两个index结尾两个substring有多少个字母时相同的。比如下边的例子

leeteet
   i  j

假如i在第四个位置，j在第七个位置，那么dp[i][j] = 3

如何用O(1)的时间来判断呢，可以用如下转移方程

if s[i]==s[j]:
    dp[i][j] = dp[i-1][j-1]

如果s[i]不等于s[j],那我们就不需要更新了。最后我们可以把所有的echo substring放进一个set里然后返回set的长度就可以了。

时间复杂度O(N^2)
空间复杂度O(N^2)

[LeetCode Link](https://leetcode-cn.com/problems/distinct-echo-substrings/)