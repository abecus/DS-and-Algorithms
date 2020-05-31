"""
_________________________140. Word Break II_________________________
Difficulty: Hard		Likes: 1662		Dislikes: 353		Solution: Available
Total Accepted: 215.1K		Total Submission: 707.1K		Acceptance Rate: 30.4%
Tags:  Backtracking, Dynamic Programming


Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, add spaces in s to construct a sentence where each word is
a valid dictionary word. Return all such possible sentences. Note:  The same
word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.  


Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""


from functools import lru_cache
def wordBreak(s, wordDict):
	l=len(s)
	@lru_cache(None)
	def foo(i):
		res=[]
		for word in wordDict:
			if word==s[i:i+len(word)]:
				if len(word)==l-i:
					res.append(word)
				else:
					for other_words in foo(i+len(word)):
						res.append(word+' '+other_words)
		return res
	return foo(0)

if __name__ == "__main__":
	# s = "catsanddog"
	# wordDict = ["cat","cats","and","sand","dog"]
	s = "pineapplepenapple"
	wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
	# s = "catsandog"
	# wordDict = ["cats", "dog", "sand", "and", "cat"]
	print(*wordBreak(s,wordDict,), sep='\n')


"""
similarQuestions::
		Word Break: Medium
		Concatenated Words: Hard
"""
