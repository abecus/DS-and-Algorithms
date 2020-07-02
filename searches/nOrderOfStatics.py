import random


def nOrderOfStatics(arr, n):
    "returns  n'th smallest element from array, n in [0...length)"
    
    def helper(left, right):
        
        # if only one element exists
        if right == left:
            return arr[left]
        
        # choose random element from the array and find its index
        idx = random.randint(left, right)
        el = arr[idx]
        arr[idx], arr[right] = arr[right], arr[idx]
        
        # keep smaller ele (smaller than el) to left
        # and larger ele to right
        i = left
        for j in range(left, right):
            if arr[j] <= el:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
        
        # put random choosen ele to its position
        arr[right], arr[i] = arr[i], arr[right]
        
        # check in which sub array the n belongs and return 
        # the result recursively
        if i==n:
            return arr[i]
        elif n<i:
            return helper(left, i - 1)
        else:
            return helper(i + 1, right)

    return helper(0, len(arr)-1)
    

if __name__ == "__main__":
    arr = [*range(20)]
    random.shuffle(arr)
    # print(arr)
    for i in range(len(arr)):
        print(nOrderOfStatics(arr, i), end=', ')