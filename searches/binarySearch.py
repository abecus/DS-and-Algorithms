def binarySearch(arr, element, where=0):
    '''
    Itype: arr(sorted list), element(comparable object)
    rtype: int
    '''
    if not arr[0]<=element<=arr[-1]:
        return -1
    
    left=0
    right=len(arr)

    while left<=right:
        mid = (left + right) // 2

        if arr[mid] < element:
            left = mid + 1

        elif arr[mid] > element:
            right = mid - 1

        else:
            return mid
    return -1

if __name__ == "__main__":
    l = [5, 6, 7, 8, 9]
    print(binarySearch(l, 87.5))
    