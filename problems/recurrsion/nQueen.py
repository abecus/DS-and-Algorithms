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
        if p==n:
            yield list("".join(aRow) for aRow in board)
            # print(board)
            return

        for col in range(n):
            if canPlace(r, col):
                board[r][col]="Q"
                yield from solveBoard(p+1, r+1, 0)
                board[r][col]="."
        return

    return [*solveBoard()]
    
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


def nQueens(n):
    """
    returns all possible board configuration where n queens can be 
    placed in n*n board, and returns an array of length n having values
    for index of row in ith column.

    Args:
        n (int): dimension
    """

    def getpos(taken, j):
        s = set()

        # add all rows to s, which can't be taken by a queen
        for t in range(j):

            # horizontally
            s.add(taken[t])

            # diagonally up
            if taken[t]-(j-t) >= 0:
                s.add(taken[t]-(j-t))

            # diagonally down
            if taken[t]+(j-t) < n:
                s.add(taken[t]+(j-t))

        for k in range(n):
            if k not in s:
                yield k

    def foo(i, j, taken):
        """[summary]
        Args:
            i (int): x coord of board
            j (int): y coord of board
            taken (List[int]): occupied row's index at ith col

        Returns:
            None
        """
        if j == n:
            # if all queens are on the board
            # return the copy of the board
            yield taken.copy()
            return 

        # take a coord where a queen can go and search for more
        for x in getpos(taken, j):
            prev = taken[j]
            taken[j] = x
            yield from foo(0, j + 1, taken)

            # backtracking part
            taken[j] = prev

    return [*foo(0, 0, [None]*n)]

if __name__ == "__main__":
    n = 5
    # for board in totalNQueens(n):
    #     print(*board, sep='\n')
    #     print(' ')
    
    print(*nQueens(n), sep='\n')
    
