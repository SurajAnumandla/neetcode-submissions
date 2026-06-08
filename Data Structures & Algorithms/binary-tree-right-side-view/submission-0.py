# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if root is None:
            return res
        q = [root]
        res = [root.val]

        while len(q) > 0:
            level = None
            for i in range(len(q)):
                node = q.pop(0)

                if node.left is not None:
                    level = node.left.val
                    q.append(node.left)

                if node.right is not None:
                    level = node.right.val
                    q.append(node.right)
            if level is not None:
                res.append(level)
        return res    