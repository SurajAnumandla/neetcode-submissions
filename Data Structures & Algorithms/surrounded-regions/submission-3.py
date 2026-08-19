class Solution:
    def dfs(self,i,j,board):
        if i< 0 or j< 0 or i>=len(board) or j >=len(board[0]) or board[i][j] != "O":
            return 
        board[i][j] = "T"
        self.dfs(i-1,j,board)
        self.dfs(i,j-1,board)
        self.dfs(i+1,j,board)
        self.dfs(i,j+1,board)
        return 
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        for i in range(0,m):
            for j in range(0,n):
                if board[i][j] == "O" and i in [0,m-1] or j in [0,n-1]:
                    self.dfs(i,j,board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"
        return 