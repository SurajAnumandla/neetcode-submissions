# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max = 0
    def depth(self, root):
        if root is None:
            return 0
        
        left = self.depth(root.left)
        right = self.depth(root.right)

        self.max = max(left+right,self.max)
        return max(left,right)+1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.max