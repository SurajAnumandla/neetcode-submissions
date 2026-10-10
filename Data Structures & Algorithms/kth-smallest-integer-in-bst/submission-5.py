# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.count = 0
        def in_order(root):
            if root is None:
                return 
            in_order(root.left)
            self.count+=1
            if self.count==k:
                self.res = root.val
                return
            in_order(root.right)
        in_order(root)
        return self.res