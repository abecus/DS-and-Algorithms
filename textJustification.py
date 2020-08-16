from functools import lru_cache
from itertools import accumulate, islice
import functools, math


m = float("inf")
def textJustification(text, lineWidth=80):
	textList = text.split(' ')
	lineWidth = max(lineWidth, *map(len, textList))
	accLength = [*accumulate(map(len, textList))]
	n = len(accLength)

	def cost(x,y):
		# calculates the cost of words in a line 
		# from index x to y inclusive
		if x==0:	lw = accLength[y]+y-x
		else:	lw = accLength[y]-accLength[x-1]+y-x
		return float('inf') if lw>lineWidth else (lineWidth-lw)**3
	
	dp=[[float("inf")]*n for _ in range(n)]

	# creates dp matrix
	for i in range(n):
		for j in range(0, n-i):
			dp[j][i+j] = cost(j,i+j)
 
	# for i in dp:	print(i)

	breakPoints = [0]*n
	costs = [float('inf')]*n

	# main loop to recreate the break-points from the dp matrix
	for i in reversed(range(n)):
		for j in reversed(range(i, n)):
			if j==n-1 and dp[i][j]!=float('inf'):
				costs[i]=dp[i][j]
				breakPoints[i]=j+1
				break

			if j+1<n and costs[i]>dp[i][j]+costs[j+1]:
				costs[i]=dp[i][j]+costs[j+1]
				breakPoints[i]=j+1

	i=0
	while i<len(textList):
		yield " ".join(islice(textList, i, breakPoints[i]))
		i=breakPoints[i]


import itertools
def textJustification2(words, l):
	# converting words into array of words
	words = words.split(' ')
	parent = {}
	accumulated_Length = [0]+[*itertools.accumulate(map(len, words))]

	def getLength(i, j):
		# returns the length of word from including spacing between them
		return accumulated_Length[j+1] - accumulated_Length[i] + j - i

	def computeCost(lineWidth, wordsLength):
		# coputes the cost functions which has to be minimized
		return pow(lineWidth - wordsLength, 3)


	@functools.lru_cache(None)
	def foo(i):
		if i == len(words):
			# no word remains
			return 0

		cost = math.inf
		for j in range(i, len(words)):
			wordLength = getLength(i, j)
			
			# check if words can fit in the a line
			if wordLength > l:	break

			# compute cost for remaining suffix array
			suffixCost = foo(j + 1)
			currCost = computeCost(l, wordLength)

			# minimise the cost and mainted parent accordingly
			if currCost + suffixCost < cost:
				cost = currCost + suffixCost
				parent[i] = j
		return cost

	# calling main function
	foo(0)

	def joinWords(i, j):
		# prettifies the words in from index [i, j)
		line = words[i: j]
		if len(line) == 1 or j == len(words):
			return (' '.join(line).ljust(l))
		else:
			n, r = divmod(l - (sum(map(len, line)) +
							   len(line)) + 1, len(line) - 1)
			narrow = ' ' * (n + 1)
			if r == 0:
				return narrow.join(line)
			else:
				wide = ' ' * (n + 2)
				return wide.join(line[:r] + [narrow.join(line[r:])])

	i = 0
	while i < len(words):
		t = parent[i]+1
		yield joinWords(i, t)
		i = t

if __name__ == "__main__":
	# file = "test.txt"
	# def getText(file):
	# 	with open(file, "r") as f:
	# 		return f.read()
	# text = getText(file).replace("\n", " ")
 
	# text = """I am the one, the one who don't need no gun to get respect upon the street"""

	text="The boy walked down the street in a carefree way, playing without notice of what was about him. He didn't hear the sound of the car as his ball careened into the road. He took a step toward it, and in doing so sealed his fate.Sometimes that's just the way it has to be. Sure, there were probably other options, but he didn't let them enter his mind. It was done and that was that. It was just the way it had to be."
	for t in textJustification2(text, 40):
		print(t)
	print(' ')
	for t in textJustification(text, 40):
		print(t)
