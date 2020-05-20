这道题用inorder traverse+迭代来做，套路如下。

1. 用while loop来进行遍历
2. 先用一个stack来存一路向左的node，知道找到最小值（利用BST的特性）
3. 弹出最小值，看是否满足条件，此题中就是这个数是否是第k个小的数
4. 如果满足直接返回值， 如果不满足那要找次小值
5. 次小值一定在当前node右枝的最左边，所以把node赋值为node.right, 然后在利用第二个while loop进入右边的最左边。因为一定有解，所以不需要最后返回值

[leetcode link](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/submissions/)