# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def dfs(preorder, inorder):
            if not preorder:
                return None
            root = TreeNode(preorder[0])
            # print (preorder, inorder)
            mid = inorder.index(preorder[0])
            
            root.left = dfs(preorder[1:mid+1], inorder[:mid])
            root.right = dfs(preorder[mid+1:], inorder[mid+1:])
            return root
        return dfs(preorder, inorder)