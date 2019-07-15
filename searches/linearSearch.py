
def linearSearch(arr, element):
    '''
    Itype: arr(list or string), element(int or str)
    rtype: int
    '''
    if element:
        for index, ele in enumerate(arr):
            if ele==element:
                return index-1
    else:
        return False