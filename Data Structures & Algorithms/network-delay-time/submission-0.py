import heapq
class Solution:
    def adj_list(self,n,edges):
        adj_list = [[] for _ in range(n+1)]

        for edge in edges:
            x = edge[0]
            y = edge[1]
            w = edge[2]
            adj_list[x].append((y,w))
        return adj_list
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = self.adj_list(n,times)

        distance = [float('inf') for _ in range(n+1)]
        distance[0] = -1
        heap = []
        distance[k] = 0
        heapq.heappush(heap,(0,k))

        while heap:
            d,node = heapq.heappop(heap)
            for v,w in adj_list[node]:
                if d+w < distance[v]:
                    distance[v] = d + w
                    heapq.heappush(heap,(distance[v],v))
        for i in range(len(distance)):
            if i!= 0 and distance[i]==float('inf'):
                return -1
        return max(distance)