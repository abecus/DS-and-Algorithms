"""
_________________________877. Stone Game_________________________
Difficulty: Medium		Likes: 401		Dislikes: 690		Solution: Available
Total Accepted: 35.1K		Total Submission: 56.2K		Acceptance Rate: 62.4%
Tags:  Dynamic Programming, Minimax, Math


Alex and Lee play a game with piles of stones.� There are an even number of�piles pilesanged in a row, and each pile has a positive integer number of stones piles[i].
The objective of the game is to end with the most�stones.� The total number of stones is odd, so there are no ties.
Alex and Lee take turns, with Alex starting first.� Each turn, a player�takes the entire pile of stones from either the beginning or the end of the row.� This continues until there are no more piles left, at which point the person with the most stones wins.
Assuming Alex and Lee play optimally, return True�if and only if Alex wins the game.
Example 1:


Input: [5,3,4,5]

Output: true

Explanation: 

Alex starts first, and can only take the first 5 or the last 5.

Say he takes the first 5, so that the row becomes [3, 4, 5].

If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.

If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.

This demonstrated that taking the first 5 was a winning move for Alex, so we return true.


�
Note:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
"""

from functools import lru_cache
def stoneGame(piles):
    
	@lru_cache(None)
	def helper(i, j):
		if (j-i)<=2:
			return max(piles)
		
		return max(
      			piles[i]+helper(i+2, j),	# both choose left, alex is alway first to choose
             	piles[i]+helper(i+1, j-1),	# alex left, lee right
               	piles[j]+helper(i+1, j-1),	# alex right, lee left
                piles[j]+helper(i, j-2)		# both right
				)
	s = sum(piles)
	return (s-helper(i=0, j=len(piles)-1))<s//2

if __name__ == "__main__":
	piles = [3,95,15,28,12,184,51,561,54,8]
	# piles = [5,3,4,5]
	print(stoneGame(piles))


"""
"""
