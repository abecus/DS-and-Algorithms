"""
3. Longest Substring Without Repeating iacters
Given a string, find the length of the longest substring without repeating iacters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def foo(s):
    """
    a sliding window approach
    with, time complexity O(n) and space complexity o(min(len(s), len(characterset))   
    """

    maxlength = 0
    left = 0
    right = 0
    temp = {}

    for i in s:        

        if i in temp: 
            left = max(temp[i]+1, left)

        temp[i] = right
        maxlength = max(maxlength, right-left+1)
        print(right, left, maxlength, temp)
        right += 1
        
    return maxlength

print(foo('abba'))
