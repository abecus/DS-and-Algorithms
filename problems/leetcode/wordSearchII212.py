"""
_________________________212. Word Search II_________________________
Difficulty: Hard		Likes: 2533		Dislikes: 110		Solution: Available
Total Accepted: 213.9K		Total Submission: 620.1K		Acceptance Rate: 34.5%
Tags:  Trie, Backtracking


Given a 2D board and a list of words from the dictionary, find all words
in the board. Each word must be constructed from letters of sequentially
adjacent cell, where "adjacent" cells are those horizontally or vertically
neighboring. The same letter cell may not be used more than once in a word.  


Example:
Input:
board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 Note:
All inputs are consist of lowercase letters a-z.
The values of words are distinct.

"""


import functools, collections
import itertools
import operator
import bisect
import array
from typing import *


class TrieNode:
	def __init__(self):
		self.children = collections.defaultdict(TrieNode)
		self.end = False

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def addWord(self, word):
		root = self.root
		for ch in word:
			root = root.children[ch]
		root.end = True

	def getRoot(self):
		return self.root


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []

        # direction = [(1,0), (0,1), (0,-1), (-1,0)]
        def findstr(i,j,t,w):
            if t.end:
                res.add(w)
                # return

            letter = board[i][j]
            board[i][j] = ""

            if i > 0 and board[i-1][j] in t.children:
                findstr(i-1, j, t.children[board[i-1][j]], w+board[i-1][j])

            if j>0 and board[i][j-1] in t.children:
                findstr(i, j-1, t.children[board[i][j-1]], w+board[i][j-1])

            if i < len(board)-1 and board[i+1][j] in t.children:
                findstr(i+1, j, t.children[board[i+1][j]], w+board[i+1][j])

            if j < len(board[0])-1 and board[i][j+1] in t.children:
                findstr(i, j+1, t.children[board[i][j+1]], w+board[i][j+1])

            board[i][j] = letter


        res = set()
        trie = Trie()
        for w in words:
            trie.addWord(w)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.root.children:
                    findstr(i, j, trie.root.children[board[i][j]], board[i][j])

        return res

# ######################## TLE for below
        # def isIn(w, idx, i, j):
        #     if idx == len(w):   
        #         return 1

        #     for x, y in direction:
        #         ci, cj = x+i, y+j
        #         if 0 <= ci < len(board) and 0 <= cj < len(board[0]) and board[ci][cj] == w[idx]:
        #             board[ci][cj] = '#'
        #             if isIn(w, idx+1, ci, cj):
        #                 board[ci][cj] = w[idx]
        #                 return 1
        #             board[ci][cj] = w[idx]
        #     return 0

        # def foo(w):
        #     for i in range(len(board)):
        #         for j in range(len(board[0])):
        #             if w[0] == board[i][j]:
        #                 board[i][j] = '#'
        #                 if isIn(w, 1, i, j):
        #                     board[i][j] = w[0]
        #                     return 1
        #                 board[i][j] = w[0]

        # res = []
        # for w in words:
        #     if foo(w):
        #         print(w)
        #         res.append(w)

        # print(board)
        # return res
# #############################################

if __name__ == "__main__":
    board=[["a"]]
    words=["a"]

    board=[["a","a"]]
    words=["aaa"]

    # board=[["a","b"],["c","d"]]
    # words=["acdb"]

    board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]

    # board = [["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"]]
    # words = ["aaaaaaaaaaaa", "aaaaaaaaaaaaa", "aaaaaaaaaaab"]

    board = [["a", "b", "c"],["a", "e", "d"],["a", "f", "g"]]
    words = ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"]

    s = Solution()
    print(s.findWords(board, words))


"""
similarQuestions::
        Word Search: Medium
        Unique Paths III: Hard
"""
