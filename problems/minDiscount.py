"""
Min discount problem -
In simple words, there is an array - prices array : [5, 4, 5, 1, 3, 3, 8, 2]
The discount on the price is the first equal to or lowest element on the right side of current price. Output the total in the end and also list of items index that will not get any discount.
For example -
5 - 4 = 1
4 - 1 = 3
5 - 1 = 4
1 - 0 = 1 (This element didn't got any discount)
3 - 3 = 0
3 - 2 = 1
8 - 2 = 6
2 - 0 = 2 (This element will also not get discount as no equal to or less than price on right).

Output -
Total = 18
Elements ID not getting discount - 3, 7
"""

def minDiscount(arr):
    '''
    itype: list
    rtype: int, list
    '''
    # take last element of arr and initialise the variables
    temp = arr.pop()
    
    localMin = temp  
    prev = temp
    total = temp
    res = [len(arr)]
    i = len(arr)-1
    
    while arr:
        temp = arr.pop()
        
        if temp>=prev:
            # if prev is <= current element add the difference to total
            total+=temp-prev
            print(temp, prev, temp-prev, total)
            
        elif temp>=localMin:
            # else if local minimun till that element from right 
            # is <= temp add the difference to total
            total+=temp-localMin
            print(temp, localMin, temp-localMin, total)
            
        else:
            # else there is its the globalmin
            # add the index to res ans element to total
            total+=temp
            res.append(i)
            print(temp, total)
            
        prev = temp  
        localMin = min(localMin, temp)
        i-=1
    
    return total, res


if __name__ == "__main__":
    arr = [5, 4, 5, 1, 3, 3, 8, 2]
    print(minDiscount(arr))