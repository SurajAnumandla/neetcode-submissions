from collections import deque
class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0]*n
        q = deque()
        adj_list = [[] for i in range(n)]
        for edge in prerequisites:
            to,frm = edge[0],edge[1]
            adj_list[frm].append(to)
            in_degree[to]+=1
        ans = []
        for i in range(n):
            if in_degree[i]==0:
                ans.append(i)
                q.append(i)
        
        while q:
            node = q.popleft()
            for edge in adj_list[node]:
                in_degree[edge]-=1
                if in_degree[edge]==0:
                    ans.append(edge)
                    q.append(edge)
        
        return ans if len(ans)==n else []