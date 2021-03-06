# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root: return []
        res = []
        self.helper(root, "", res)
        return res
    
    def helper(self, root, current, res):
        if not root.left and not root.right:
            current += str(root.val)
            res.append(current)
        if root.left:
            self.helper(root.left, current+str(root.val)+"->", res)
        if root.right:
            self.helper(root.right, current+str(root.val)+"->", res)