def binarySearch(arr, element, where=0):
    '''
    Itype: arr(sorted list), element(comparable object)
    rtype: int
    '''
    if not arr[0]<=element<=arr[-1]:
        return -1
    
    i = 1
    while i<len(arr) and arr[i]<=element:
        i = i * 2

    left = i // 2
    right = min(len(arr), i)
    
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
    l = [*range(50)]
    print(binarySearch(l, 5))
    