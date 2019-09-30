"""
_________________________921. Minimum Add to Make Parentheses Valid_________________________
Difficulty: Medium		Likes: 360		Dislikes: 27		Solution: Available
Total Accepted: 34.9K		Total Submission: 49.5K		Acceptance Rate: 70.6%
Tags:  Stack, Greedy


Given a string�S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.
Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB�(A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
�
Example 1:
Input: "())"
Output: 1

Example 2:
Input: "((("
Output: 3

Example 3:
Input: "()"
Output: 0

Example 4:
Input: "()))(("
Output: 4

Note:

S.length <= 1000
S only consists of '(' and ')' characters.

"""

from array import array
def minAddToMakeValid(S):
    s = array('u', [])
    res=0
    for i in S:
        if not s and i==')':
            res+=1
        elif i==')':
            s.pop()
        else:
            s.append(i)
            
    return res+len(s)

if __name__ == "__main__":
    S = "())"
    S = "((("
    S = "()"
    S = "()))(("
    S = ""
    print(minAddToMakeValid(S,))


"""
"""
