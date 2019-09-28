"""
You are developing an OCR (Optical Character Recognition) application to translate handwritten text to digital text.
Your application is still evolving and is not perfect yet. Your application aims to avoid false positives[wrongly recognized characters].

In order to do this,
1. Your application currently replaces a character that it could not recognize with a "$" character.
2. The application outputs a "@" character, if there is a sequence of characters that it failed to recognize. [this sequence could be of size >= 0] .
You want to know how accurate the application currently is.
You are given two strings: String H representing hand-written text, 
and a String I representing the application's interpretation of that text.
Determine whether the application's interpretation of the text was correct.

Constraints:
1 <= length of Strings H, I <= 10 ^ 5
H, I can contain : 1. Any alphabet, 2. White Spaces

Example 1:
Input:
H = "aa"
I = "a"
Output:
False
Explanation: "a" does not match the hand-written string "aa".

Example 2:
Input:
H = "aa"
I = "@"
Output:
True 
Explanation: 
Application failed to recognize the character sequence "aa" and replaced it with "@"
This is a valid translation given the application's limitation.

Example 3:
Input:
H = "cb"
I = "$a"
Output:
False 
Explanation: 
Application seemingly failed to recognize character "c" and hence instead printed a "$"
However, the application seems to have wrongly recognized "b" as "a".

Example 4:
Input:
H = "adceb"
I = "@a@b"
Output:
True
Explanation: 
The first '@' matches the empty sequence, while the second '@' matches the sequence "dce"  that application couldn't recognize.

Example 5:
Input:
H = "acdcb"
I = "a@c$b"
Output:
False 
"""


def ocr(H, I):
    """
    creating dp array for checking if prefix of string (original) is true for 
    given length of prefix output of OCR and building on that till last all prefix
    or last case
    """
    dp = [[False for _ in range(len(I)+1)] for _ in range(len(H)+1)]
    dp[0][0] = True
    
    for i in range(1, len(dp[0])):
        if I[i-1] == '@':
            dp[0][i] = True 
            
    for i in range(1, len(H)+1):
        for j in range(1, len(I)+1):
            
            if H[i-1] == I[j-1] or I[j-1] == '$':
                dp[i][j] = dp[i-1][j-1]
                
            elif I[j-1] == '@':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
                
            else:
                dp[i][j] = False
                
    return dp[-1][-1]

if __name__ == "__main__":
    # H = "acdcb"
    # I = "a@c$b"       # False
    
    # H = "cb"
    # I = "$a"        # False
    
    H = "adceb"
    I = "@a@b"        # True
    
    # H = "aa"
    # I = "a"     #False

    # H = "aa"
    # I = "@"     #True 
    
    print(ocr(H, I))
    print(H, I)
