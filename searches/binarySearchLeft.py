def binarySearchLeft(arr, element):
    '''
    Itype: arr(sorted list), element(comparable object)
    rtype: int (first index where element can be inserted)
    '''
        
    left=0
    right=len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < element:
            left = mid + 1
        else:
            right = mid

    return left

if __name__ == "__main__":
    l = [5, 6, 6.4, 7, 7, 7]
    print(binarySearchLeft(l, 7))
        