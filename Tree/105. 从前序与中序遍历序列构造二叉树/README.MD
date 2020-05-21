这道题是用preorder和inorder遍历后的array来重新建树， 因为建树要先建root，然后再建左树和右树，所以很自然的想到递归，把建左右两树的工作交个下一个方程。

那么如何把左右两树需要的材料准确传递给子树呢？拿题中例子来说

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

首先preorder的第一个元素就是root的值，然后在inorder中找到root的坐标叫做mid，在inorder中mid左边的数都输root的left tree，mid右边的数都是root的right tree，所以传给子树的inorder array就可以由mid自然的分开了，那么我们可不可以找到传给子树的preorder array呢，这个就是解开本题的钥匙，我们发现mid这个位置在preorder中也可以把左树和右树分开，但不同的是，在preorder中，左树是preorder[1:mid+1],右树是preorder[mid+1:],有了这个条件那我们就可以精确定位左，root，右三部分的preorder和inorder了。这个性质要牢记。

[LeetCode Link](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)