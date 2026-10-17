class Solution:
    def dfs(self,i,adjList,visited):
        visited[i]=True
        for node in adjList[i]:
            if not visited[node]:
                self.dfs(node,adjList,visited)
        return 
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False]*n
        adjList = [[] for i in range(n)]
        for conn in edges:
            start,end = conn[0],conn[1]
            adjList[start].append(end)
            adjList[end].append(start)

        count = 0
        for i in range(n):
            if not visited[i]:
                self.dfs(i,adjList,visited)
                count+=1
        return count