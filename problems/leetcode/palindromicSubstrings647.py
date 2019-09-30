"""
_________________________647. Palindromic Substrings_________________________
Difficulty: Medium		Likes: 1656		Dislikes: 85		Solution: Available
Total Accepted: 121.4K		Total Submission: 209.2K		Acceptance Rate: 58.0%
Tags:  String, Dynamic Programming


Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
Example 1:


Input: "abc"

Output: 3

Explanation: Three palindromic strings: "a", "b", "c".


�
Example 2:


Input: "aaa"

Output: 6

Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


�
Note:

The input string length won't exceed 1000.

�
"""

def countSubstrings(s):
    l = len(s)
    
    def helper(i, j):
        c = 0
        while i>=0 and j<l and s[i]==s[j]:
            c+=1
            i-=1
            j+=1
        return c
    
    res = 0
    for i in range(l):
        # expands from single source
        res+=helper(i, i)
        if i+1<l:
            # expands from double (left, right) source
            res+=helper(i, i+1)
        
    return res

if __name__ == "__main__":
    s = "abc"
    # s = "abcdcb"
    print(countSubstrings(s,))


"""
similarQuestions::
        Longest Palindromic Substring: Medium
        Longest Palindromic Subsequence: Medium
        Palindromic Substrings: Medium
"""
