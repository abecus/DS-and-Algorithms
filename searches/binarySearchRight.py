def binarySearchRight(arr, element):
    '''
    Itype: arr(sorted list), element(comparable object)
    rtype: int (last index where element can be inserted)
    '''
        
    left=0
    right=len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > element:
            right = mid 
        else:
            left = mid + 1

    return left

if __name__ == "__main__":
    l = [5, 6, 7, 7, 7, 8, 9]
    print(binarySearchRight(l, 9))