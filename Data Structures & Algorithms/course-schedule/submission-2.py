from collections import deque
class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for i in range(n)]
        in_degree = [0]*n
        for edge in prerequisites:
            to,frm = edge[0],edge[1]
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
                    res.append(val)
                    q.append(val)
        return len(res)==n