"""
_________________________784. Letter Case Permutation_________________________
Difficulty: Easy		Likes: 909		Dislikes: 95		Solution: Available
Total Accepted: 70.3K		Total Submission: 114.5K		Acceptance Rate: 61.3%
Tags:  Backtracking, Bit Manipulation


Given a string S, we can transform every letter individually to
be lowercase or uppercase to create another string. 
Return a list of all possible strings we could create. 
 


Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:
S will be a string with length between 1 and 12.
S will consist only of letters or digits.

"""


def letterCasePermutation(S):
	res=set()
	l=len(S)
	S=[*S]
	def f(i, s):
		for j in range(i, l+1):
			if j==l:	res.add("".join(s))
			elif s[j].islower():
				s[j]=s[j].upper()
				f(j+1, s)
				s[j]=s[j].lower()
	f(0, S)
	return  res

if __name__ == "__main__":
	S = "a1b2"
	print(letterCasePermutation(S,))


"""
similarQuestions::
		Subsets: Medium
		Brace Expansion: Medium
"""
