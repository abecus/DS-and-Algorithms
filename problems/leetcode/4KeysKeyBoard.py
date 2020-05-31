"""
Imagine you have a special keyboard with the following keys: 
Key 1:  Prints 'A' on screen
Key 2: (Ctrl-A): Select screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending it
				 after what has already been printed. 

If you can only press the keyboard for N times (with the above four
keys), write a program to produce maximum numbers of A's. That is to
say, the input parameter is N (No. of keys that you can press), the 
output is M (No. of As that you can produce).
"""

def maxA(n):

	from functools import lru_cache
	@lru_cache(None)
	def f(x,copied,steps):
		if steps>n:
			return -float('inf')
		if steps==n:
			return x
		return max(
			f(x+1, copied, steps+1),		# key_1
			f(x+x, x, steps+3),				# key_2
			f(x+copied, copied, steps+1)	# key_4
		)

	temp = f(1, 0, 1)
	print(f.cache_info())
	print(temp)
 
if __name__ == "__main__":
	maxA(20)
