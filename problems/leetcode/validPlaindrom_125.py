"""
125. Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
"""

import re

def foo(s):
    s = "".join(re.findall(r'\w+', s.lower()))
    left = 0
    right = len(s)-1
    
    while left < right:
        if s[left] != s[right]:
            return False
        right -= 1
        left += 1
    return True

a = "A man, a plan, a canal: Panama"
b = "race a car"
print(foo(b))
