"""
540. Single Element in a Sorted Array
Share
Given a sorted array consisting of only integers where every element appears exactly twice except for one element which appears exactly once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.
"""

def nonDuplicate(arr):
    if len(arr)<2:
        return arr[0]
    
    right = len(arr)-1
    left = 0
    i = 0
    
    while right-left>0 and  i<10:
        print(left, right)
        i+=1
        middle = (right + left)//2
        
        if arr[middle] == arr[middle-1]:
            if (middle - left + 1) % 2  == 0:
                left = middle+1
            else:
                right = middle
                
        elif arr[middle] == arr[middle+1]:
            if (right - middle + 1) % 2  == 0:
                right = middle-1
            else:
                left = middle
        else:
            return arr[middle]
    
    # print(right, left)
    return arr[right]

if __name__ == "__main__":
    a = [1, 1,2]     #10
    # a = [1,1,2,3,3,4,4,8,8]    #2
    print(nonDuplicate(a))