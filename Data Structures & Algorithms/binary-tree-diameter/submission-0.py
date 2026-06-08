# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self,root, res):
        if root is None:
            return 0
        left_height = self.maxDepth(root.left,res)
        right_height = self.maxDepth(root.right,res)

        curr  = left_height + right_height
        res["max"] = max(res["max"],curr)
        return max(left_height,right_height) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        res = {"max":0}
        left = self.maxDepth(root.left,res)
        right = self.maxDepth(root.right,res)
        curr = left + right
        return max(res["max"],curr)