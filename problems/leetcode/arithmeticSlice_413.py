"""
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
For example, these are arithmetic sequence:
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic.
1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.
A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.
The function should return the number of arithmetic slices in the array A.

Example:
A = [1, 2, 3, 4]
return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""
def foo(arr):
    
    c = 0
    j=1
    i=0
    while j<len(arr):
        t = arr[j-1] - arr[j]
        while j+i+1<=len(arr)-1 and arr[j+i]-arr[j+1+i]==t:
            c +=1
            i +=1
        else:
            j+=1
            i=0
            continue
        j=i
        i=0
    return c

l = [1,3,5,7,9,15,20,25,28,29]
m = [1, 2, 3, 5, 7]
print(foo(m))