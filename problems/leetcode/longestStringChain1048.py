"""
_________________________1048. Longest String Chain_________________________
Difficulty: Medium		Likes: 228		Dislikes: 15		Solution: None
Total Accepted: 15.5K		Total Submission: 30.6K		Acceptance Rate: 50.8%
Tags:  Hash Table, Dynamic Programming


Given a list of words, each word consists of English lowercase letters.
Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".
A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.
Return the longest possible length of a word chain with words chosen from the given list of words.
 
Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".

 
Note:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.


 
"""


def longestStrChain(words):
    l =len(words)
    
    def isPred( w1, w2):
        if len(w1)+1==len(w2):
            c = 0
            j = i = 0
            l = len(w1)
            while i<l:
                if w1[i]!=w2[i]:
                    if c==0:
                        c+=1
                        j+=1
                        continue
                    else:
                      return 0
                i+=1
                j+=1
            return 1
        return 0
    
    from functools import lru_cache
    @lru_cache(None)
    def helper(i):
        
        for j in range(l):
            pass
            
        

    return isPred('abc', 'aabc')


if __name__ == "__main__":
    words = ["a","b","ba","bca","bda","bdca"]
    print(longestStrChain(words,))


"""
"""
