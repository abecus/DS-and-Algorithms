count = []
def totalNQueens(n):
    board = [["."]*n for _ in range(n)]

    def canPlace(r, c):
        for i in range(n):
            #straight top-down and straight left-right
            if board[r][i]==1 or board[i][c]=="Q":
                return 0
            
            # down right
            if r+i<n and c+i<n and board[r+i][c+i]=="Q":
                return 0
            
            #up-left
            if 0<=r-i and 0<=c-i and board[r-i][c-i]=="Q":
                return 0

            #up-right
            if 0<=r-i and c+i<n and board[r-i][c+i]=="Q":
                return 0
            
            #down-right
            if r+i<n and 0<=c-i and board[r+i][c-i]=="Q":
                return 0
        return 1

    def solveBoard(p=0, r=0 ,c=0):
        global count
        if p==n:
            count.append(list("".join(aRow) for aRow in board))
            # print(board)
            return

        for col in range(n):
            if canPlace(r, col):
                board[r][col]="Q"
                solveBoard(p+1, r+1, 0)
                board[r][col]="."
        return
    
    solveBoard()
    # def DFS(queens, xy_dif, xy_sum):
    #         p = len(queens)
    #         if p==n:
    #             result.append(queens)
    #             return None
    #         for q in range(n):
    #             if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
    #                 DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
    # result = []
    # DFS([],[],[])
    # return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]


totalNQueens(9)
print(count)
