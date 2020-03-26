"""
_________________________917. Reverse Only Letters_________________________
Difficulty: Easy		Likes: 385		Dislikes: 30		Solution: Available
Total Accepted: 44.1K		Total Submission: 77.4K		Acceptance Rate: 57.0%
Tags:  String


Given a string S, return the "reversed" string where all
characters that are not a letter stay in the same place,
and all letters reverse their positions.            


Example 1:
Input: "ab-cd"
Output: "dc-ba"

Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 Note:
S.length <= 100
33 <= S[i].ASCIIcode <= 122 S doesn't contain \ or "
"""


def reverseOnlyLetters(S):
	if len(S)==1:	return S
	i=0
	n=len(S)
	j=n-1
	res=[]
	while i<n and j>=0:
		if not S[i].isalpha():
			res.append(S[i])
			i+=1
			continue
		if S[j].isalpha():
			res.append(S[j])
			j-=1
			i+=1
		else:	j-=1

	if i<n:	res.extend([ch for ch in S[i:]])
	if j>=0:	res.extend([ch for ch in reversed(S[:j+1])])
	return "".join(res)

if __name__ == "__main__":
	# S = "Test1ng-Leet=code-Q!"
	# S="dc-ba"
	S="-"
	print(reverseOnlyLetters(S,))


"""
"""
