"""
_________________________338. Counting Bits_________________________
Difficulty: Medium		Likes: 1643		Dislikes: 117		Solution: Available
Total Accepted: 192.3K		Total Submission: 292.5K		Acceptance Rate: 65.7%
Tags:  Dynamic Programming, Bit Manipulation


Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
"""
from array import array

def countBits(num):
    base = [0, 1, 1]
    ans = array('i', base)
    
    if num<3:
        return base[:num+1]
    
    for i in range(3, num+1):
        if i%2==0:
            ans.append(ans[i//2])
        else:
            ans.append(ans[i-1]+1)
    
    return ans



if __name__ == "__main__":
    num = 5
    print(countBits(num))
    

"""
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

similarQuestions::

                Number of 1 Bits: Easy

"""