"""
_________________________211. Add and Search Word - Data structure design_________________________
Difficulty: Medium		Likes: 1919		Dislikes: 94		Solution: Available
Total Accepted: 195.6K		Total Submission: 526.9K		Acceptance Rate: 37.1%
Tags:  Design, Trie, Backtracking


Design a data structure that supports the following two operations:

 void addWord(word)
 bool search(word)
  search(word) can search
a literal word or a regular expression string containing only
letters a-z or .. A . means it can represent any one letter. 


Example:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

"""


import functools
import itertools
import operator
import bisect
import array
import collections


class TreeNode():
    def __init__(self):
        self.children = [None]*26
        self.end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    @staticmethod
    def mapper(x):
        return ord(x)-97

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        temp = self.root
        for i in word:
            if temp.children[self.mapper(i)] == None:
                temp.children[self.mapper(i)] = TreeNode()
            temp = temp.children[self.mapper(i)]
        temp.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        stack = [(0, self.root)]

        while stack:
            i, root = stack.pop()

            if i == len(word):
                if root.end==True:
                    return True

            if word[i] == '.':
                for child in root.children:
                    if child != None:
                        stack.append((i+1, child))

            elif root.children[self.mapper(word[i])] != None:
                stack.append((i+1, root.children[self.mapper(word[i])]))

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == "__main__":
    # todo = ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
    # words = [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]

    todo = ["WordDictionary","addWord","addWord","addWord","addWord","addWord","addWord","addWord","addWord","search","search","search","search","search","search","search","search","search","search"]
    words = [[],["ran"],["rune"],["runner"],["runs"],["add"],["adds"],["adder"],["addee"],["r.n"],["ru.n.e"],["add"],["add."],["adde."],[".an."],["...s"],["....e."],["......."],["..n.r"]]

    wordDict = WordDictionary()
    for i in range(1, len(todo)):
        if todo[i]=='addWord':
            print('isin:', words[i])
            wordDict.addWord(words[i][0])
        elif todo[i]=='search':
            print('search:', words[i])
            print(wordDict.search(words[i][0]))




"""
similarQuestions::
		Implement Trie (Prefix Tree): Medium
		Prefix and Suffix Search: Hard
"""
