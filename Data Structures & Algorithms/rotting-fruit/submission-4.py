from collections import deque
class Solution:
    def __init__(self):
        self._max = float('-inf')
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j,0))
        if fresh == 0:
            return 0
        while q:
            i,j,c = q.popleft()

            for x,y in ((0,-1),(0,1),(-1,0),(1,0)):
                nx,ny = x+i,y+j
                if nx>=0 and ny>=0 and nx<len(grid) and ny<len(grid[0]):
                    if grid[nx][ny]==1:    
                        grid[nx][ny] = 2
                        fresh-=1
                        q.append((nx,ny,c+1))
                        self._max = max(self._max,c+1)
        if fresh!=0:
            self._max = -1
        else:
            if self._max == float('-inf'):
                self._max = -1
        return self._max