"""
_________________________680. Valid Palindrome II_________________________
Difficulty: Easy		Likes: 935		Dislikes: 67		Solution: Available
Total Accepted: 96.8K		Total Submission: 276K		Acceptance Rate: 35.1%
Tags:  String



Given a non-empty string s, you may delete at most one character.  Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True


Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.


Note:

The string will only contain lowercase characters a-z.
The maximum length of the string is 50000.

"""


def validPalindrome(s):
    def is_pali_range(i, j):
        return all(s[k] == s[j-k+i] for k in range(i, j))

    for i in range(len(s)//2):
        if s[i] != s[~i]:
            j = len(s) - 1 - i
            return is_pali_range(i+1, j) or is_pali_range(i, j-1)
    return True

if __name__ == "__main__":
    s = "aba"
    s = "abc"
    # s = "eedede"
    s = "abbdca"
    s = "abbda"
    print(validPalindrome(s,))


"""
similarQuestions::
        Valid Palindrome: Easy
"""
