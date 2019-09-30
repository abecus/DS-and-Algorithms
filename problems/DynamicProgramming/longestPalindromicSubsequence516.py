"""
_________________________516. Longest Palindromic Subsequence_________________________
Difficulty: Medium		Likes: 1117		Dislikes: 142		Solution: None
Total Accepted: 74.6K		Total Submission: 153.4K		Acceptance Rate: 48.6%
Tags:  Dynamic Programming

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: 
"bbbab"

Output: 
4
One possible longest palindromic subsequence is "bbbb".

Example 2:
Input:
"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

"""

from functools import lru_cache
def longestPalindromeSubseq(s):
    l = len(s)
    
    @lru_cache(None)
    def helper(i, j, s=s):
        if i==j:
            return 1
        
        if s[i]==s[j] and i+1==j:
            return 2
        
        if s[i]==s[j]:
            return 2+helper(i+1, j-1)
        
        return max(helper(i+1, j),
                   helper(i, j-1))
    a = helper(0, l-1)
    print(helper.cache_info())
    return a

if __name__ == "__main__":
    s = "bbbab"
    # s= "azdaza"
    print(longestPalindromeSubseq(s,))


"""
similarQuestions::
        Longest Palindromic Substring: Medium
        Palindromic Substrings: Medium
        Count Different Palindromic Subsequences: Hard
        Longest Common Subsequence: Medium
"""
