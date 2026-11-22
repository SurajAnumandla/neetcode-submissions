from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        
        while q:
            for v in range(len(q)):
                i,j,c = q.popleft()

                for x,y in ((0,-1),(0,1),(-1,0),(1,0)):
                    nx,ny = i+x,j+y
                    if nx>=0 and ny>=0 and nx<len(grid) and ny<len(grid[0]):
                        if grid[nx][ny]==2147483647:
                            grid[nx][ny] = c+1
                            q.append((nx,ny,c+1))
