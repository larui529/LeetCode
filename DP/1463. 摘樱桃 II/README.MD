典型的DP多状态转移题目，可以用一个三维数组来
dp[i][j][k] 来表示在第i行，左robot在j位置，右robot在k位置时可以得到的最大值。

然后从前一个状态可以退出下一个状态， 即
moves = [-1,0,1] # 在i状态下可以向左下，正下，右下方移动
dp[i+1][j+jj][k+kk] = max(dp[i+1][j+jj][k+kk], dp[i][j][k]+grid[i+1][j+jj]+grid[i+1][k+kk])
因为同样的i,j,k状态可能有好几种方法走到，所以要取最大值。

需要注意的是在哪些情况下我们不仅如此这个更新，

1. 出界的情况下，比如j+jj<0 or j+jj>=n
2. 两个robot走到了同一个地方， j+jj == k+kk
3. 如果上一个状态是不可能状态，我们初始化dp的时候可以把每个状态都设为-float('inf')，这样如果dp[i][j][k]==-float('inf')，那我们就知道这个状态在之前就不可能得到，那自然不会有由它推出来的下一个状态了

初始化的dp[0][0][n-1]就是左右机器人初始位置采到最多的樱桃值
dp[0][0][n-1] = grid[0][0] + grid[0][n-1]

最后遍历dp[-1]的所有位置找到最大值

[LeetCode Link](https://leetcode-cn.com/problems/cherry-pickup-ii/)