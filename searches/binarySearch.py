def binarySearch(arr, element, where=0):
    '''
    Itype: arr(sorted list), element(comparable object)
    rtype: int
    '''
    if element:

        mid = (len(arr)-1)//2
        if arr[mid]==element:
            return mid+where
        
        elif arr[mid] > element:
            return binarySearch(arr[:mid], element, where)
        
        else:
            return binarySearch(arr[mid+1:], element, where+mid+1)

    else:
        return False

if __name__ == "__main__":
    l = [5, 6, 7, 8, 9]
    print(binarySearch(l, 9))
    