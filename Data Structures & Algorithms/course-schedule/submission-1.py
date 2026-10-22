from collections import deque
class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        ans = []
        adj_list = [[] for i in range(n)]
        in_degree = [0]*n 
        for to,frm in prerequisites:
            # frm->to
            adj_list[frm].append(to)
            in_degree[to]+=1
        
        for i in range(n):
            if in_degree[i]==0:
                ans.append(i)
                q.append(i)
        while q:
            node = q.popleft()
            for near in adj_list[node]:
                in_degree[near]-=1
                if in_degree[near]==0:
                    ans.append(near)
                    q.append(near)
        return len(ans)==n
