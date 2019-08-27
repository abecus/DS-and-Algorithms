"""
Alice is a kindergarten teacher. She wants to give some candies 
to the children in her class.  All the children sit in a line 
and each of them has a rating score according to his or her 
performance in the class.  Alice wants to give at least 1 candy 
to each child. If two children sit next to each other, then the 
one with the higher rating must get more candies. Alice wants 
to minimize the total number of candies she must buy.

For example, assume her students' ratings are [4, 6, 4, 5, 6, 2].
She gives the students candy in the following minimal 
amounts: [1, 2, 1, 2, 3, 1]. She must buy a minimum of 10 candies.
"""


def candies(n, arr):
    s = 0
    i = 0
    prev = 1
    
    
    def decTill(i):
        # given an starting index it returns the 
        # last index uptill sequence is decreasing 
        while i<n-1:
            if arr[i+1]<arr[i]:
                i+=1
            else:
                break
        return i

    # for first element doing it only 
    # for if first element happens to be 
    # greater than the second element, works also for 
    # if first it less then second element
    j = decTill(i) - i + 1 
    s+=j*(j+1)//2
    i+=j
    
    # final loop for rest of elements
    while i<n:
        
        temp = prev+1 if arr[i]>arr[i-1] else 0
        j = decTill(i)-i+1 
        
        if j>=temp:
            s += j*(j+1)//2
            prev = 1
        
        else:
            s += temp + j*(j+1)//2 - j            
            prev = 1 if j > 1 else temp

        i+=j
    return s
        
        
if __name__ == "__main__":
    
    arr0 = [2, 4, 2, 6, 1, 7, 8, 9, 4, 9] #19
    arr1 = [6, 2, 3] #5
    arr2 = [2,4,3,5,2,6,4,5] #12
    arr3 = [2,4,2,6,1,7,8,9,2,1] #19
    arr4 = [1,2,2] #4
    arr5 = [9, 2, 3, 6, 5, 4, 3, 2, 2, 2]  #22
    arr6 = [9, 8, 7, 7, 6, 6, 5, 4, 3]   #19
    l = [arr0, arr1, arr2, arr3, arr4, arr5, arr6]
    
    for arr in l:
        print(candies(len(arr), arr))
    