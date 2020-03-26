"""
_________________________467. Unique Substrings in Wraparound String_________________________
Difficulty: Medium		Likes: 469		Dislikes: 75		Solution: None
Total Accepted: 22.1K		Total Submission: 63.3K		Acceptance Rate: 34.8%
Tags:  Dynamic Programming


Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.
Note: p consists of only lowercase English letters and the size of p might be over 10000.
Example 1:

Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.


Example 2:

Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.


Example 3:

Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.

"""
import collections

class Solution:
	def findSubstringInWraproundString(self, p: str) -> int:
		dp=collections.defaultdict(int)
		length, prevChar = 0, "a"
		for char in p:
			if (ord(char)-ord(prevChar))%26==1:	length+=1
			else:	length=1
			dp[char]=max(dp[char], length)
			prevChar=char
		return sum(dp.values())

if __name__ == "__main__":
	p = "cab"
	sol=Solution()
	print(sol.findSubstringInWraproundString(p,))


"""
"""
