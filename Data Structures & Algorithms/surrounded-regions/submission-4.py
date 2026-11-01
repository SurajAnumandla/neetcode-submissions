class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return board
        m = len(board)
        n = len(board[0])
        fr = 0
        lr = m-1
        fc = 0
        lc = n-1
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return 
            if board[i][j]!="O":
                return
            if board[i][j]=="O":
                board[i][j]="T"

            dfs(i,j-1)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i+1,j)   

        for i in range(n):
            dfs(fr,i)
            dfs(lr,i)
        
        for i in range(m):
            dfs(i,fc)
            dfs(i,lc)

        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="X"
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=="T":
                    board[i][j]="O"
        