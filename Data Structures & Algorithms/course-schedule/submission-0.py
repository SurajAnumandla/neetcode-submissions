from collections import deque
class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        ans = []
        adj_list = [[] for _ in range(n)]
        in_degree = [0]*n
        for x,y in prerequisites:
            adj_list[y].append(x)
            in_degree[x]+=1
        
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)
                ans.append(i)

        while q:
            node = q.popleft()
            for v in adj_list[node]:
                in_degree[v]-=1
                if in_degree[v] == 0:
                    q.append(v)
                    ans.append(v)
        return len(ans)==n