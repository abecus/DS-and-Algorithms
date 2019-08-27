"""
You are given a large document as input. Within a document you can assume that words are separated by a white-case character. 
After this you are given another array of prefixes, for every prefix you have to provide array of integers which are  different 
starting locations where the prefix can be found in the document.
Prefix need to be matched in a case insensitive manner. In case prefix is not found return -1.

Function Description:
Implement function getLocations which accepts the following parameters.
document - a string denoting a document
prefixes - a single dimensional string array containing a list of prefixes.

The function should return a 2D integer array whose each row contains an array of the starting locations of the corresponding prefix in the document.

Input format for custom testing:
First line contains a string representing the document
Second line contains an integer n denoting the number of prefixes
Next n lines contain an integer array representing the prefixes.

Output format:
2D array with each row representing an array of starting locations of each prefix.

Sample testcase:
Input
a aa Aaa abca bca  ---> document

5   ----> number of prefixes with next 5 lines representing the prefixes.

a   
bc
aA
abc
d

Output
0 2 5 9 ---> starting locations of prefix 'a'
14    -----> starting location of prefix 'bc'
2 5   -----> starting locations of prefix 'aA'
9      -----> starting location of prefix 'abc'
-1    -----> prefix 'd' not found, hence -1
"""

import re

def check(s1, s2):
    if len(s1)<len(s2):
        return False
    
    for i in range(len(s2)):
        if s2[i]==s1[i]:
            continue
        
        else:
            return False
        
    else:
      return True
  
def prefixMatch(doc, l):
    """
    a bouteforce way with time complexity O(|doc|*|l|)
    
    itype: doc:str
    
    rtype: l: list of str to check
    """
    ret = []    
    doc = doc.split(' ')
    
    for tocheck in l:
        index = 0
        temp = []
        f = 0
        for withStr in doc:
            if check(withStr.lower(), tocheck.lower()):
                temp.append(index)
                f = 1
                  
            index+= len(withStr)+1
            
        if f==0:
            temp.append(-1)
        ret.append(temp)
                   
    return ret
        
if __name__ == "__main__":
    doc = "a aa Aaa abca bca"
    l = ["a","bc","aA","abc","d"]
    print(prefixMatch(doc, l))
        