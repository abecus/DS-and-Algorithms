"""
_________________________1021. Remove Outermost Parentheses_________________________
Difficulty: Easy		Likes: 234		Dislikes: 349		Solution: None
Total Accepted: 50K		Total Submission: 66.5K		Acceptance Rate: 75.3%
Tags:  Stack


A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
 
Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".


Example 2:

Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".


Example 3:

Input: "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

 


Note:

S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string



 

"""


def removeOuterParentheses(S):
    s = ""
    l = []
    res = ""
    for i in S:
        s+=i
        try:
            if l[-1]!=i:
                l.pop()
                if len(l) == 0:
                    res+=s[1:-1]
                    s=''
                continue
        except: pass
        l.append(i)
    return res
        

if __name__ == "__main__":
    S = "(()())(())"
    S = "()()"
    S = "(()())(())(()(()))"
    S = ""
    print(removeOuterParentheses(S,))


"""
"""
