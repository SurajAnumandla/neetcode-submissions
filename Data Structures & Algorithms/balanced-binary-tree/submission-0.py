# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = True

    def tree_height(self, root):
        if root is None:
            return 0

        left_height = self.tree_height(root.left)
        right_height = self.tree_height(root.right)

        if abs(left_height - right_height) > 1:
            self.ans = False

        return max(left_height,right_height) + 1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.tree_height(root)
        return self.ans