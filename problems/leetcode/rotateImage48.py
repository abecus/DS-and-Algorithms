"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Note:
You have to rotate the image in-place, which means you have to 
modify the input 2D matrix directly. DO NOT allocate another 
2D matrix and do the rotation.

Example 1:
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 
rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""

def rot(matrix):
    N=len(matrix)-1
    for d in range((N+1)>>1):   # row
        for i in range(d,N-d):  # col
            temp = matrix[d][i]
            matrix[d][i] = matrix[N-i][d]
            matrix[N-i][d] = matrix[N-d][N-i]
            matrix[N-d][N-i] = matrix[i][N-d]
            matrix[i][N-d] = temp
    print(matrix)


if __name__ == "__main__":
    rot([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
])
# m=np.arange(1,10).reshape((3,3))
# print(np.rot90(m, k=-1))
# t=np.array([[0,2],[-2,0]])