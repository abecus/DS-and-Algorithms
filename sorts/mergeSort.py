import random


def mergeSort(arr):
    """
    itype: list
    rtype: list
    """
    def merge(l1, l2):
        """
        merges two sorted list in other sorted list
        """
        i=0
        j=0
        temp = []
        
        while i<len(l1) and j<len(l2):
            if l1[i]>l2[j]:
                temp.append(l2[j])
                j+=1
            
            elif l1[i]<l2[j]:
                temp.append(l1[i])
                i+=1
            
            else:
                temp.extend([l1[i], l2[j]])
                i+=1
                j+=1 
            
        if j==len(l2):
            temp.extend(l1[i:])
        
        else:
            temp.extend(l2[j:])
        
        return temp         
    
                
    def helper(arr):
        """
        calls the merge subrutine on each level from bottom up in tree
        """
        if len(arr)==1:
            return arr
        
        n = len(arr)//2
        return merge(helper(arr[:n]), helper(arr[n:]))
    
    return helper(arr)
    
    
if __name__ == "__main__":
    
    l = [random.randint(1, 13) for _ in range(13)]
    print(mergeSort(l))