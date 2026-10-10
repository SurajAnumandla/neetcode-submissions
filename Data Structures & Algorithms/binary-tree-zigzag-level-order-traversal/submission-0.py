# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def level(self,root):
        res = []
        if not root:
            return res
        q = deque()
        q.append(root)
        count = 0
        while q:
            ans = []
            count+=1
            for i in range(len(q)):
                node = q.popleft()
                ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if ans:
                if count%2==0:
                    res.append(ans[::-1])
                else:
                    res.append(ans)
        return res

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.level(root)
        