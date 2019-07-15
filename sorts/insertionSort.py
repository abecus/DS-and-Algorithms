
def insertionSort(arr, i=1):
    """
    Itype: list
    rtype: list
    """
    if i==len(arr):
        return arr

    else:

        a=1
        while True:
            """
            checking if left element to previous sorted array is
            larger than the last element of previous sorted array,
            if it is then swaping
            """

            if arr[i-a+1] < arr[i-a] and i-a+1 != 0:
                arr[i-a+1], arr[i-a] = arr[i-a], arr[i-a+1]
                a+=1

            else:
                break
        
        return insertionSort(arr, i+1)


if __name__ == "__main__":

    l = [i for i in reversed(range(10))]
    print(insertionSort(l))
