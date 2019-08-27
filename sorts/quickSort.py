import random

def quickSort(arr):
    """
    itype: list
    rtype: list
    """    
    def helper(arr, left, right):
        """
        returns te index were the partition has been done
        
        rtype: int
        """
        i = left        
        # keep the initial index as base
        
        pivot = arr[right]      
        # want to find the position of last element in arr
        
        for j in range(left, right):
            # loop through all possible lower elements
            
            if arr[j] <= pivot:
                # keep the elements smaller than the pivot 
                # to left by swapping them with index i and increase 
                # the index by one 
                
                arr[j], arr[i] = arr[i], arr[j]
                i+=1
                
        arr[i], arr[right] = arr[right], arr[i]
        # finally swap the element (the pivot element) to its right place
        # and return the index of partition
        return i
                
                
    def mainHelper(arr, left, right):
        if left<right:
            # if lenght of sub array is more than one
            # find the pivot 
            pivot = helper(arr, left, right)
            
            # do same sort on left and right sub arrays 
            # except the pivot element
            mainHelper(arr, pivot+1, right)
            mainHelper(arr, left, pivot-1)
        
    mainHelper(arr, 0, len(arr)-1)
    return arr

if __name__ == "__main__":
    # a = [random.randint(0, 14) for _ in range(5)]
    a = [0,10,1]
    print(quickSort(a))