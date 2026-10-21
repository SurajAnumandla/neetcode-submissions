import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for i in range(n+1)]
        for edge in times:
            to = edge[0]-1
            frm = edge[1]-1
            w = edge[2]
            adj_list[to].append((frm,w))
        heap = []
        dist = [float('inf')]*(n)
        heapq.heappush(heap,(0,k-1))
        dist[k-1] = 0
        visited = [False] * (n)
        while heap:
            d,frm = heapq.heappop(heap)
            for edge in adj_list[frm]:
                to,w = edge
                curr = d + w
                if curr < dist[to]:
                    dist[to] = curr
                    heapq.heappush(heap,(curr,to))
        ans = max(dist)
        if ans==float('inf'):
            return -1
        return ans