"""
_________________________1255. Maximum Score Words Formed by Letters_________________________
Difficulty: Hard		Likes: 195		Dislikes: 18		Solution: None
Total Accepted: 8.9K		Total Submission: 12.8K		Acceptance Rate: 69.3%
Tags:  Bit Manipulation


Given      a      list      of      words,      list      of      single letters
(might be repeating) and score of every character.                              
Return   the   maximum  score  of  any  valid  set  of  words  formed  by  using
the given letters (words[i] cannot be used two or more times).                  
It   is   not   necessary   to   use   all   characters   in  letters  and  each
letter   can   only   be   used  once.  Score  of  letters 'a',  'b',  'c',  ...
,'z' is given by score[0], score[1], ... , score[25] respectively.              
                                                                                
																				


Example 1:  Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
 Output: 23
 Score  a=1, c=9, d=5, g=3, o=2
 Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
 Words "dad" and "dog" only get a score of 21.
 
Example 2:  Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
 Output: 27
 Score  a=4, b=4, c=4, x=5, z=10
 Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
 Word "xxxz" only get a score of 25.
 
Example 3:  Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
 Output: 0
 Letter "e" can only be used once.
    1 <= words.length <= 14 1 <= words[i].length <= 15 1 <= letters.length <= 100 letters[i].length == 1 score.length == 26 0 <= score[i] <= 10 words[i], letters[i] contains only lower case English letters.  
"""


import functools, itertools, operator, bisect, array, collections 
from typing import *


class Solution:
	def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
		
		def foo(i, words, counts, score, profit):
			nonlocal res
			
			if i==len(words):
				res = max(res, profit)
				return 0
			
			# profit = 0
			if all(counts[w] >= words[i][w] for w in words[i].keys()):
				s = 0
				for w in words[i].keys():
					counts[w] -= words[i][w]
					# profit += words[i][w] * score[ord(w)-ord('a')]
					s += words[i][w] * score[ord(w)-ord('a')]

				# profit += 
				foo(i+1, words, counts, score, profit+s)
				# res = max(res, profit)
				
				for w in words[i].keys():                    
					counts[w] += words[i][w]
					# profit -= words[i][w] * score[ord(w)-ord('a')]

			# profit += 
			foo(i+1, words, counts, score, profit)
			# res = max(res, profit)
				
			# return profit
					
		res = 0
		words = [collections.Counter(word) for word in words]
		counts = collections.Counter(letters)
		print(foo(0, words, counts, score, 0))
		return res
		


if __name__ == "__main__":
	words = ["dog","cat","dad","good"]
	letters = ["a","a","c","d","d","d","g","o","o"]
	score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

	words = ["xxxz","ax","bx","cx"]
	letters = ["z","a","b","c","x","x","x"]
	score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]

	words = ["leetcode"]
	letters = ["l","e","t","c","o","d"]
	score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
	
	s = Solution()
	print(s.maxScoreWords(words, letters, score))


"""
"""
