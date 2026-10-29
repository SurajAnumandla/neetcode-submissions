from collections import deque
class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for i in range(n)]
        in_degree = [0]*n
        for edge in prerequisites:
            to,frm = edge
            adj_list[frm].append(to)
            in_degree[to]+=1
        q = deque()
        res = []
        for i in range(n):
            if in_degree[i]==0:
                q.append(i)
                res.append(i)
        while q:
            node = q.popleft()
            for val in adj_list[node]:
                in_degree[val]-=1
                if in_degree[val]==0:
                    q.append(val)
                    res.append(val)
        return res if len(res)==n else []
