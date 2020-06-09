"""
_________________________208. Implement Trie (Prefix Tree)_________________________
Difficulty: Medium		Likes: 3016		Dislikes: 49		Solution: Available
Total Accepted: 309.1K		Total Submission: 644.2K		Acceptance Rate: 48.0%
Tags:  Trie, Design


Implement a trie with insert, search, and startsWith methods. 


Example:
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

"""

import sortedcontainers
class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.endsHere = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=Node('.')
        
    def _insert(self, word, i, root):
        if i == len(word):
            root.endsHere = True
            return
        node = Node(word[i])
        root.children[word[i]] = node
        return self._insert(word, i+1, node)
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        i=0
        temp=self.root
        while i != len(word) and word[i] in temp.children:
            temp = temp.children[word[i]]
            i += 1
        self._insert(word, i, temp)
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        i=0
        temp=self.root
        while i != len(word) and word[i] in temp.children:
            temp = temp.children[word[i]]
            i += 1
        
        return False if i<len(word) else i==len(word) and temp.endsHere

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        i=0
        temp=self.root
        while i != len(prefix) and prefix[i] in temp.children:
            temp = temp.children[prefix[i]]
            i += 1
        return i==len(prefix)        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    trie = Trie()
    print(trie.insert("apple"))
    print(trie.search("apple"))    # returns true
    print(trie.search("app"))      # returns false
    print(trie.search("apples"))   # returns false
    print(trie.startsWith("app"))  # returns true
    print(trie.insert("app"))   
    print(trie.search("app"))      # returns true


"""
similarQuestions::
		Add and Search Word - Data structure design: Medium
		Design Search Autocomplete System: Hard
		Replace Words: Medium
		Implement Magic Dictionary: Medium
"""
