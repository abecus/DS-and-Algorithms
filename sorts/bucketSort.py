import random


def bucketSort(arr):
    """
    only integer values are allowed
    
    itype: list
    rtype: list
    """
    counter = {}
    
    def helper(arr):
        min, max = float('inf'), -float('inf')
            
        for i in arr:
            # finding min and max in one go efficiently
            if i < min:
                min = i
            elif i > max:
                max = i
        
        for i in range(min, max+1):
            # initialising the hashmap
            counter[i] = 0
            
        for i in arr:
            # counting the values to hashmap
            counter[i] += 1
               
        lst = []
        for i, j in counter.items():
            for k in range(j):
                # appending counted values to lst by their frequency
                lst.append(i)
    
        return lst

    if len(arr)>1:
        return helper(arr)
    else:
        return arr


if __name__ == "__main__":
        
    a = [random.randint(0, 1000) for _ in range(100)]
    print(bucketSort(a))    
                              