class Solution:
    def dfs(self,i,j,board):
        if i<0 or j<0 or i>=len(board) or j>= len(board[0]):
            return
        if board[i][j]=="X":
            return
        if board[i][j]=="T":
            return
        board[i][j]="T"
        self.dfs(i,j-1,board)
        self.dfs(i,j+1,board)
        self.dfs(i-1,j,board)
        self.dfs(i+1,j,board)
        return 
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        
        for i in range(0,n):
            if board[0][i]=="O":
                self.dfs(0,i,board)
            if board[m-1][i]=="O":
                self.dfs(m-1,i,board)

        for i in range(0,m):
            if board[i][0]=="O":
                self.dfs(i,0,board)
            if board[i][n-1]=="O":
                self.dfs(i,n-1,board)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="T":
                    board[i][j]="O"
        return 