"""
_________________________941. Valid Mountain Array_________________________
Difficulty: Easy		Likes: 205		Dislikes: 51		Solution: Available
Total Accepted: 28.6K		Total Submission: 81.2K		Acceptance Rate: 35.2%
Tags:  Array


Given an array A of integers, return true if and only if it is a valid mountain array.
Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
    
A[0] < A[1] < ... A[i-1] < A[i] 
A[i] > A[i+1] > ... > A[A.length - 1]



 
Example 1:

Input: [2,1]
Output: false


Example 2:
Input: [3,5,5]
Output: false

Example 3:
Input: [0,3,2,1]
Output: true
 
Note:
0 <= A.length <= 10000
0 <= A[i] <= 10000 
"""

def validMountainArray(A):
    length = len(A)
    if length<3:
        return False
    i=0
    while i<length-1 and A[i]<A[i+1]:
        i+=1
        
    if i==length-1 or i==0:
        return False     

    while i<length-1 and A[i+1]<A[i]:
        i+=1
        
    return i==length-1
    
    
if __name__ == "__main__":
    A = [2,1,5]
    # A = [0,3,2,1]
    # A = [3,5,5]
    # A = [0,0,1,0,0,0,0,0,0,0]
    print(validMountainArray(A,))


"""
"""
