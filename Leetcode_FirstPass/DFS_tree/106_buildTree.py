# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder == None: return []
        if postorder == None: return []
        while inorder:
            index = inorder.index(postorder.pop())
            root = TreeNode(inorder[index])     
            #  cannot switch the order for right and left, contrast to the pre-order, in-order traversal
            root.right = self.buildTree(inorder[index+1:], postorder)
            root.left = self.buildTree(inorder[:index], postorder)
            return root