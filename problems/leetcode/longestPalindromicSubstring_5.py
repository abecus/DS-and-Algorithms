"""
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""
startIndex = 0
maxLength = 1
def foo(s):
    length = len(s)
       
    def helper(left, right):
            global maxLength, startIndex

            while left>=0 and right<length and s[left]==s[right]:
                currentLenght = right-left+1

                if currentLenght > maxLength:
                    maxLength = currentLenght
                    startIndex = left
                
                left -=1
                right +=1

    for i in range(length):
        helper(i-1, i+1)        
        helper(i, i+1)

    return s[startIndex: startIndex+maxLength]

a = 'cbbd'
b = 'babad'
print(foo(a))
