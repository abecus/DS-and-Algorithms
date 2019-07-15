        
def bubbleSort(arr):
    """
    Itype: list
    rtype: list
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i):
            """
            traverse the array from 0 to n-i-1 
            Swap if the element found is greater 
            than the next element
            """
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
        

if __name__ == "__main__":

    l = [i for i in reversed(range(10))]
    print(bubbleSort(l))
