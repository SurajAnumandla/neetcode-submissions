class Solution:
    def dfs(self, i, adjList, visited):
        visited[i] = True
        for x in adjList[i]:
            if not visited[x]:
                self.dfs(x,adjList,visited)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = []

        for i in range(n):
            adjList.append([])
        
        for edge in edges:
            x = edge[0]
            y = edge[1]

            adjList[x].append(y)
            adjList[y].append(x)
        visited = [False]*n
        ans = 0
        for i in range(n):
            if not visited[i]:
                self.dfs(i,adjList,visited)
                ans+=1
        return ans
        
