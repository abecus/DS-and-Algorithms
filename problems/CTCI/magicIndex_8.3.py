def magicIndex(arr):
    n = len(arr)-1
    
    def helper(arr, i, j, temp, n):
        print((i, j, temp, arr[i]))
        if n<0:
            return -1
        
        if arr[i]>i:
            j=i
            temp=i
            i=int((temp+i+0.5)//2)
            return helper(arr, i, j, temp, n-1)
            
        elif arr[i]<i:
            temp = i
            i = int((i+j+0.5)//2)
            return helper(arr, i, j, temp, n-1)
        
        elif arr[i] == i:
            return arr[i]
            
    return helper(arr, int(n//2), n, int(n//2), n//2)       
        
if __name__ == "__main__":
    l = [-2, -1, 1, 3, 5, 6]
    print(magicIndex(l))