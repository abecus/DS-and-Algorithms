
def matPrenth(matrixes):
    """
    itype: matrixes: list of tuples having (row, column)
    rtype: list
    """ 
    dp = [[float('inf') if i!=j else 0 for i in range(len(matrixes))] for j in range(len(matrixes))]

    for row in range(1, len(dp)):
        for col in range(row, len(dp[0])):
            for k in range(1, row):
                pass

    

if __name__ == "__main__":
    mats = [(40, 20),
            (20, 30),
            (30, 10),
            # (10, 30)
            ]
    print(matPrenth(mats))