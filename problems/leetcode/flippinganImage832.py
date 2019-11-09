"""
_________________________832. Flipping an Image_________________________
Difficulty: Easy		Likes: 617		Dislikes: 130		Solution: Available
Total Accepted: 128K		Total Submission: 173.9K		Acceptance Rate: 73.6%
Tags:  Array


Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

Notes:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1

"""


def flipAndInvertImage(A):
    rl = len(A)
    l = len(A[0])//2
    for r in range(rl):
        i = 0
        while i<l:
            A[r][-1-i], A[r][i] = A[r][i]^1, A[r][-1-i]^1
            i+=1
    if l*2!=len(A[0]):
        for i in range(rl):
            A[i][l] ^= 1 
    return A

if __name__ == "__main__":
    A = [[1,1,0],[1,0,1],[0,0,0]]
        # [[1,0,0],[0,1,0],[1,1,1]]
        
    A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
        # [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    
    A = [[1]]
    print(flipAndInvertImage(A,))


"""
"""
