# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lca(self,root,p,q):
        if root.val<p.val and root.val >q.val:
            return root
        
        if root.val == p.val or root.val == q.val:
            return root
        
        if root.val < p.val and root.val < q.val:
            return self.lca(root.right,p,q)
        
        if root.val > p.val and root.val > q.val:
            return self.lca(root.left,p,q)
        return root
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.lca(root,p,q)