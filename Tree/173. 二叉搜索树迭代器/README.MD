这道题还是利用了BST的中序遍历（inorder traverse），我们可以用递归把所有的数按从小到大放入一个数组中，但这样的话空间复杂度就是O(N),比较大，也可以用迭代，先找到最左边的node，然后再去找最左边稍微偏右一点的node，也就是用一个stack把从小到大的元素依次压进去，如果顶端元素不是当前的最小值，那一定可以继续向左遍历知道最左端，然后是当前root，再最后遍历root.right. 这样的好处是空间复杂度为O(H),H为树的深度。

[LeetCode Link](https://leetcode-cn.com/problems/binary-search-tree-iterator/)