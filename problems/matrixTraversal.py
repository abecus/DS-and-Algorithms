def spiralPrint(m, n, a) : 
    k = 0; l = 0
  
    ''' k - starting row index 
        m - ending row index 
        l - starting column index 
        n - ending column index 
        i - iterator '''
      
  
    while (k < m and l < n) : 
          
        # Print the first row from 
        # the remaining rows  
        for i in range(l, n) : 
            print(a[k][i]) 
              
        k += 1
  
        # Print the last column from 
        # the remaining columns  
        for i in range(k, m) : 
            print(a[i][n - 1]) 
              
        n -= 1
  
        # Print the last row from 
        # the remaining rows  
        if ( k < m) : 
              
            for i in range(n - 1, (l - 1), -1) : 
                print(a[m - 1][i]) 
              
            m -= 1
          
        # Print the first column from 
        # the remaining columns  
        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                print(a[i][l]) 
              
            l += 1

def spiralMatrix(mat):
    nRow = len(mat)
    nCol = len(mat[0])
    atRow=0
    atCol=0
    while atRow<nRow and atCol<nCol:
        for i in range(atCol,nCol):
            print(mat[atRow][i])
        atRow+=1
        
        for i in range(atRow,nRow):
            print(mat[i][nCol-1])
        nCol-=1

        if atRow<nRow:
            for i in reversed(range(atCol,nCol)):
                print(mat[nRow-1][i])
            nRow-=1
            
        if atCol<nCol:
            for i in reversed(range(atRow,nRow)):
                print(mat[i][atCol])
            atCol+=1
        
        
def diagonalMatrix(mat):
    nRow = len(mat)
    nCol = len(mat[0])
    for row in range(nRow):
        col=0
        while col<nCol and row>=0:
            print(mat[row][col], end=" ")
            row-=1
            col+=1
        print(' ')
        
    for col in range(1, nCol):
        row=nRow-1
        while row>=0 and col<nCol:
            print(mat[row][col], end=" ")
            row-=1
            col+=1
        print(' ')


if __name__ == "__main__":
    M = [
        [1,  2,  3,  4], 
        [5,  6,  7,  8], 
        [9,  10, 11, 12], 
        [13, 14, 15, 16], 
        [17, 18, 19, 20]
        ]
    
    a = [
        [1,  2,  3,  4,  5], 
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9]
        ]

    # R = 3; C = 5
    # spiralPrint(R, C, a)

    # spiralMatrix(a)
    diagonalMatrix(M)