"""
Given a matrix that contains only the characters '0' and '1',
find the biggest plus sign (+) formed by 1s in this matrix and 
return its size. Size, in this case, indicates the length of 
the plus sign's edges. In order to be a valid plus sign, the 
edges must be of equal length.

For example, a plus sign with a size of k in matrix starts at 
cell (x, y). The plus sign's edges are (x - k, y), (x - k + 1, y), 
..., (x + k, y) and (x, y - k), (x, y - k + 1), ..., (x, y + k), 
all with a length of k.

Example

For

  matrix = ["0010010", 
            "1010101",
            "1111111", 
            "0010000",
            "0000000"]
the output should be biggestPlus(matrix) = 1.

Here, the biggest plus sign is centered at cell (2, 2) (0-based) and 
has a size of 1 since the downward facing edge is short.

Input/Output

[execution time limit] 9 seconds (py3)

[input] array.string matrix

A matrix containing only the symbols '0' and '1'. It is guaranteed that 
there is at least one '1' in matrix.

Guaranteed constraints:
1 ≤ inputArray.length ≤ 1000,
1 ≤ inputArray[i].length ≤ 5000.

[output] integer

The size of the biggest plus sign formed by 1s in matrix.
"""

import functools
import sys
sys.setrecursionlimit(10000)


def biggestPlus(matrix):
    # dp = [[math.inf]*c for _ in range(r)]
    # for i in range(r):
    #     dp[i][0] = int(matrix[i][0])
    #     dp[i][-1] = int(matrix[i][-1])
    # for i in range(c):
    #     dp[0][i] = int(matrix[0][i])
    #     dp[-1][i] = int(matrix[-1][i])

    # def foo(d):
    #     if d=='down':
    #         for i in range(1, r-1):
    #             for j in range(1, c-1):
    #                 if matrix[i][j]=='0':
    #                     dp[i][j] = 0
    #                 else:   dp[i][j] = 1+dp[i-1][j]

    #     elif d=='up':
    #         for i in reversed(range(1, r-1)):
    #             for j in range(1, c-1):
    #                 if matrix[i][j]=='1':
    #                     dp[i][j] = max(dp[i][j], 1+dp[i+1][j])

    #     elif d=='right':
    #         for j in range(1, c-1):
    #             for i in range(1, r-1):
    #                 if matrix[i][j]=='1':
    #                     dp[i][j] = max(dp[i][j], 1+dp[i][j-1])
    #     else:
    #         for j in reversed(range(1, c-1)):
    #             for i in range(1, r-1):
    #                 if matrix[i][j]=='1':
    #                     dp[i][j] = max(dp[i][j], 1+dp[i][j+1])

    # foo("down")
    # foo("up")
    # foo("right")
    # foo('left')
    # print(*dp, sep='\n')
    # return max(map(max, dp))-1

    # ######################################################
    # r = len(matrix)
    # c = len(matrix[0])

    # @functools.lru_cache(None)
    # def foo(i,j,d):
    #     if not (0<=i<r and 0<=j<c) or matrix[i][j]=='0':  return 0
    #     elif d==0:  return 1+foo(i-1,j,d)
    #     elif d==1:  return 1+foo(i+1,j,d)
    #     elif d==2:  return 1+foo(i,j-1,d)
    #     else:       return 1+foo(i,j+1,d)

    # res = 0
    # for i in range(r):
    #     for j in range(c):
    #         if matrix[i][j]=='1':
    #             res = max(res, min(foo(i,j,0),foo(i,j,1),foo(i,j,2),foo(i,j,3))-1)

    # print(foo.cache_info())
    # return res

    # ######################################################
    r = len(matrix)
    c = len(matrix[0])

    @functools.lru_cache(None)
    def left(i, j):
        if i == 0 or i == r-1 or j == 0 or j == c-1 or matrix[i][j] == '0':
            return int(matrix[i][j])
        return 1+left(i, j-1)

    @functools.lru_cache(None)
    def right(i, j):
        if i == 0 or i == r-1 or j == 0 or j == c-1 or matrix[i][j] == '0':
            return int(matrix[i][j])
        return 1+right(i, j+1)

    @functools.lru_cache(None)
    def up(i, j):
        if i == 0 or i == r-1 or j == 0 or j == c-1 or matrix[i][j] == '0':
            return int(matrix[i][j])
        return 1+up(i-1, j)

    @functools.lru_cache(None)
    def down(i, j):
        if i == 0 or i == r-1 or j == 0 or j == c-1 or matrix[i][j] == '0':
            return int(matrix[i][j])
        return 1+down(i+1, j)

    res = 0
    for i in range(1, r-1):
        for j in range(1, c-1):
            if matrix[i][j] == '1':
                lv = left(i, j)
                rv = right(i, j)
                uv = up(i, j)
                dv = down(i, j)
                temp = min(lv, rv, uv, dv)
                res = max(res, temp-1)

    print(left.cache_info())
    print(right.cache_info())
    print(up.cache_info())
    print(down.cache_info())
    return res

    # # left[j][j], right[i][j], top[i][j] and
    # # bottom[i][j] store maximum number of
    # # consecutive 1's present to the left,
    # # right, top and bottom of mat[i][j] including
    # # cell(i, j) respectively
    # left = [[0]*c for y in range(r)]
    # right = left.copy()
    # top = left.copy()
    # bottom = left.copy()
    # mat = matrix
    # # initialize above four matrix
    # for i in range(c):

    #     # initialize first row of top
    #     top[0][i] = int(mat[0][i] )

    #     # initialize last row of bottom
    #     bottom[- 1][i] = int(mat[- 1][i] )

    # for i in range(r):
    #     # initialize first column of left
    #     left[i][0] = int(mat[i][0])

    #     # initialize last column of right
    #     right[i][- 1] = int(mat[i][- 1])

    # # fill all cells of above four matrix
    # for i in range(r):
    #     for j in range(1, c):

    #         # calculate left matrix (filled
    #         # left to right)
    #         if (mat[i][j] == '1'):
    #             left[i][j] = left[i][j - 1] + 1
    #         else:
    #             left[i][j] = 0

    #         # calculate top matrix
    #         if (mat[j][i] == '1'):
    #             top[j][i] = top[j - 1][i] + 1
    #         else:
    #             top[j][i] = 0

    #         # calculate new value of j to calculate
    #         # value of bottom(i, j) and right(i, j)
    #         j = c - 1 - j

    #         # calculate bottom matrix
    #         if (mat[j][i] == "1"):
    #             bottom[j][i] = bottom[j + 1][i] + 1
    #         else:
    #             bottom[j][i] = 0

    #         # calculate right matrix
    #         if (mat[i][j] == "1"):
    #             right[i][j] = right[i][j + 1] + 1
    #         else:
    #             right[i][j] = 0

    #         # revert back to old j
    #         j = c - 1 - j

    # # n stores length of longest '+'
    # # found so far
    # n = 0

    # # compute longest +
    # for i in range(r):
    #     for j in range(c):

    #         # find minimum of left(i, j),
    #         # right(i, j), top(i, j), bottom(i, j)
    #         l = min(min(top[i][j], bottom[i][j]),
    #                 min(left[i][j], right[i][j]))

    #         # largest + would be formed by
    #         # a cell that has maximum value
    #         if(l > n):
    #             n = l

    # # 4 directions of length n - 1 and 1
    # # for middle cell
    # if (n):
    #     return 4 * (n - 1) + 1

    # # matrix contains all 0's
    # return 0


if __name__ == "__main__":
    matrix = ["0010010",
              "1010101",
              "1111111",
              "0010000",
              "0000000"]
    matrix = ["1",
              "1",
              "1",
              "1",
              "1",
              "1"]
    matrix = ["11111",
              "11111",
              "11111",
              "11111",
              "11111"]
    print(biggestPlus(matrix))
