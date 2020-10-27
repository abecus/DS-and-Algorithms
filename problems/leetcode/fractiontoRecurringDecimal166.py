"""
_________________________166. Fraction to Recurring Decimal_________________________
Difficulty: Medium		Likes: 979		Dislikes: 2035		Solution: Available
Total Accepted: 136.4K		Total Submission: 621.9K		Acceptance Rate: 21.9%
Tags:  Hash Table, Math


Given    two    integers    representing    the    numerator   and   denominator
of a fraction, return the fraction in string format.                            
If the fractional part is repeating, enclose the repeating part in parentheses. 
If multiple answers are possible, return any of them.                           
It      is      guaranteed     that     the     length     of     the     answer
string is less than 104 for all the given inputs.                               
                                                                                
                                                                                


Example 1: Input: numerator = 1, denominator = 2
 Output: "0.5"
 
Example 2: Input: numerator = 2, denominator = 1
 Output: "2"
 
Example 3: Input: numerator = 2, denominator = 3
 Output: "0.(6)"
 
Example 4: Input: numerator = 4, denominator = 333
 Output: "0.(012)"
 
Example 5: Input: numerator = 1, denominator = 5
 Output: "0.2"
     -231 <= numerator, denominator <= 231 - 1 denominator != 0  
"""


import functools, itertools, operator, bisect, array, collections 
from typing import * 

class Solution:
	def fractionToDecimal(self, N: int, D: int) -> str:
		if N==0:    return '0'
		if D==1:    return str(N)
		if N%D==0:  return str(int(N//D))
		
		d = {}
		if (N<0 and D<0) or (N>0 and D>0):
			res = ''
		else:
			res = '-'
			N = abs(N)
			D = abs(D)
		
		div, N = divmod(N, D)
		
		if div==0:
			res+='0.'
		else:
			res+=str(div)+'.'
		
		N*=10
		idx = len(res)
		while N:
			div, t = divmod(N, D)
			if N in d:
				return res[:d[N]]+'('+res[d[N]:]+')'
			
			if div==0:
				res+='0'
			else:
				res+=str(div)
				
			d[N] = idx
			idx+=1
			N = t*10
			
		return res        


if __name__ == "__main__":
  s = Solution()
  print(s.fractionToDecimal(-50, 8))


"""
"""
