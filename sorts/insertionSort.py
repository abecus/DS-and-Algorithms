
def insertionSort(arr):
    """
    Itype: list
    rtype: list
    """
    for i in range(1, len(arr)):
        j = i
        while j>0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

if __name__ == "__main__":

    l = [i for i in reversed(range(10))]
    insertionSort(l)
    print(l)
