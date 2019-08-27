"""
You can perform the following operations on the string, "a":

Capitalize zero or more of "a"'s lowercase letters.
Delete all of the remaining lowercase letters in "a".
Given two strings, a and b, determine if it's possible to make a equal to b as described.

For example, given 'a=AbcDE" and "b=ABDE", in a we can convert b and delete c to match b .
If "a=AbcDE" and "b=AFDE", matching is not possible because letters may only be capitalized 
or discarded, not changed.
"""


def abbreviation(a, b):
    # initialisation
    la = len(a)
    lb = len(b)

    # creating dp array
    dp = [[False for _ in range(lb+1)] for _ in range(la+1)]
    dp[0][0] = True
    for i in range(1, la+1):
        if a[i-1].islower():
            dp[i][0] = dp[i-1][0]
        else:
            dp[i][0] = False

    # main loop 
    for i in range(1, la+1):
        # i is for rows
        k = i-1
        char_a = a[k]
        
        for j in range(1, lb+1):
            # j is for columns
            l = j-1
            char_b = b[l]

            if char_a.islower():
                # if character is lower
                
                if char_a.upper() == char_b:
                    # look for upper left "or" straight up 
                    # whichever is true
                    dp[i][j] = dp[k][l] or dp[k][j] 
                    continue
                
                else:
                    # take the straight up value
                    dp[i][j] = dp[k][j]
            
            elif char_a == char_b:
                # take the upper left value
                dp[i][j] = dp[k][l]

    
    return dp[-1][-1]
