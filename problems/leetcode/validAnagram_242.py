"""
242. Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.
"""

def foo(s, t):
    temp = {}
    
    if len(s)!=len(t):
        return False
    
    for i in s:
        if i in temp:
            temp[i] +=1
    
        else:
            temp[i] = 1
    
    for i in t:
        if i not in temp or not temp[i]:
            return False
        
        else:
            temp[i] -=1
    
    return True


s = "anagram"; t = "nagaram"
# s = "rat"; t = "car"
# s = "aacc"; t = "ccac"
print(foo(s, t))    
   
    