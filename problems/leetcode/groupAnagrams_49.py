"""
49. Group Anagrams
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Output:
[
  ["ate", "eat", "tea"], 
  ["nat", "tan"], 
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""

def foo(arr):
    mapping = {}
    
    for i in arr:    
        temp = "".join(sorted([j for j in i]))

        if temp in mapping:
            mapping[temp].append(i)
            
        else:
            mapping[temp] = [i]
            
    
    return list(mapping.values())



a = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(foo(a))    
        