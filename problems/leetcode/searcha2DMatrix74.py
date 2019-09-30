"""
_________________________74. Search a 2D Matrix_________________________
Difficulty: Medium		Likes: 1035		Dislikes: 119		Solution: Available
Total Accepted: 251.4K		Total Submission: 712K		Acceptance Rate: 35.3%
Tags:  Array, Binary Search


Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:


Input:

matrix = [

  [1,   3,  5,  7],

  [10, 11, 16, 20],

  [23, 30, 34, 50]

]

target = 3

Output: true


Example 2:


Input:

matrix = [

  [1,   3,  5,  7],

  [10, 11, 16, 20],

  [23, 30, 34, 50]

]

target = 13

Output: false
"""


def searchMatrix(matrix, target):
    
    r = len(matrix)
    try:
        c = len(matrix[0])
    except:
        return False

    if (not c) or (not r):
        # sanity check
        return False
    
    def get_row(r, c, matrix, target):
        mid = (r-1)//2
        u = r-1
        l = 0
        # A binary search on last entry of rows
        # loop through the last entry of each row to get 
        # the row of interest (least greater row than the target)
        while u>=0 and l<r and u>l:
            ele = matrix[mid][-1]
            
            if ele>target :
                # if target is less than the current value
                if matrix[mid-1][-1]<target:
                    # to check for if its the least greater row
                    break
                u = mid
                mid = (l+u)//2
                
            elif ele<target:
                # if target is greater than the current value(last entry of row)
                if matrix[mid+1][-1]>target or (mid+1)==u:
                    mid+=1
                    break
                l = mid
                mid = (l+u)//2   
            
            else:
                # they equal
                return mid
            
        return mid
    
    
    from bisect import bisect_right
    
    mid = get_row(r, c, matrix, target)
    # binary search on that row to get the pos+1 as index 
    # where pos is where the target should be in the row
    idx = bisect_right(matrix[mid], target)
    if idx==0:
        return matrix[mid][0]==target
    
    return matrix[mid][idx-1]==target


if __name__ == "__main__":
    matrix =[[1,3,5,7],
            [10,11,16,20],
            [23,30,34,50],
            [60,70,80,90]]
    l = []
    for i in matrix:
        l.extend(i)
    for i in [-10, 100, 15, 21]:
        # i=16    
        target = i
        print(i, searchMatrix([],target))


"""
similarQuestions::
    Search a 2D Matrix II: Medium
"""
