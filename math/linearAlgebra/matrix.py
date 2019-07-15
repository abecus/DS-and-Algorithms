
def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    for row in matrix:
        assert len(row) == columns,  "Not Even a Matrix, rows size don't match"

    if rows==columns:
        for i in range(rows - 1):
            for j in range(i+1, columns):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        return matrix
    
    else:
        mat = [[] for _ in range(columns)]

        for i in range(rows):
            for j in range(columns):
                mat[j].append(matrix[i][j])
    
        return mat


def broadcast(num, shape):
    n, m = shape
    return [[num for _ in range(m)] for _ in range(n)]


def multiply(mat1, mat2):

    if not isinstance(mat1, float) and not isinstance(mat1, int):

        rows1 = len(mat1)
        columns1 = len(mat1[0])
        rows2 = len(mat2)
        columns2 = len(mat2[0])

        assert columns1 == rows2,  "Can't Multiply, rows and columns dont match"

        def adder(a1, a2):
            for i in range(len(a1)):
                a1[i] += a2[i]
            return a1

        

        mat = []
        temp = [0 for _ in range(rows2)]

        for row1 in mat1:
            i = 0

            for row2 in mat2:
                temp = adder([row1[i]*j for j in row2], temp)
                i += 1

            mat.append(temp)                            
        return mat

    else:
        return  [
                 [mat1*i for i in mat2[j]] 
                 for j in range(len(mat2[0]))
                ]
        

def dotProduct(mat1, mat2):
    mat1Trans = transpose(mat1)
    return multiply(mat1Trans, mat2)


if __name__ == "__main__":
    mat33 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9] 
    ]

    mat32 = [
        [1, 2],
        [4, 5],
        [7, 8] 
    ]

    mat31 = [
        [1],
        [2],
        [3]
    ]

    # print(mat13)
    # print(transpose(mat13))
    # print(multiply(transpose(mat31), mat31))
    print(dotProduct(mat31, mat31))
