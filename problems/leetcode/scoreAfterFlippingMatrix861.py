"""
_________________________861. Score After Flipping Matrix_________________________
Difficulty: Medium		Likes: 305		Dislikes: 82		Solution: Available
Total Accepted: 15K		Total Submission: 21.2K		Acceptance Rate: 70.5%
Tags:  Greedy


We have a two dimensional matrix�A where each value is 0 or 1.
A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.
After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
Return the highest possible�score.

Example 1:


Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]

Output: 39

Explanation:

Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].

0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
Note:

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j]�is 0 or 1.


"""

def matrixScore(A):
    rows = len(A)
    cols = len(A[0])
    
    def calc(T):
        return sum(int(''.join(map(str, i)), base=2) for i in T)

    def trans(r, c, d):
        if d==0:
            # for rows
            for i in range(cols):
                A[r][i] = 1^A[r][i]
        else:
            # for cols
            for i in range(rows):
                A[i][c] = 1^A[i][c]
            
    for row in range(rows):
        if A[row][0] == 0:
            trans(row, 0, 0)
            
    for col in range(cols):
        # count ones in that column
        ones = sum(A[i][col] for i in range(rows))
        if ones<rows-ones:
            trans(0, col, 1)
            
    # print(A)
    return calc(A)      

if __name__ == "__main__":
    A = [[0,0,1,1],
         [1,0,1,0],
         [1,1,0,0]]
    
    # A = [[0,0,1],
    #      [1,0,1]]
    # ans
    # [[1,1,1,1],[1,0,0,1],[1,1,1,1]] 
    print(matrixScore(A,))


"""
"""
