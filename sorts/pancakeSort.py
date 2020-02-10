def pancakeSort(A):
    def findMinIndex(i, l, A=A):
        m = float('inf')
        idx = i
        for j in range(i, l):
            if m>A[j]:
                m = A[j]
                idx = j
        return idx
    
    l = len(A)
    # for i in range(l):
    #     idx = findMax(i, l) # find min index from i and furthur on
    #     A[idx:] = [*reversed(A[idx:])]
    #     A[i:] = [*reversed(A[i:])]
    print(findMinIndex(0, len(A)))
    return A

if __name__ == "__main__":
    A = [3,2,4,1]
    print(pancakeSort(A,))
