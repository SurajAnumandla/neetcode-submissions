import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for i in range(n)]
        heap = []
        for edge in times:
            frm,to,w = edge[0]-1,edge[1]-1,edge[2]
            adj_list[frm].append((to,w))
        dis = [float('inf')]*n
        s = k-1
        dis[s] = 0
        heapq.heappush(heap,(0,s))
        while heap:
            d,node = heapq.heappop(heap)
            for edge in adj_list[node]:
                to,w = edge[0],edge[1]
                if d+w<dis[to]:
                    dis[to] = d+w
                    heapq.heappush(heap,(d+w,to))
                
        ans = max(dis)
        return -1 if ans==float('inf') else ans