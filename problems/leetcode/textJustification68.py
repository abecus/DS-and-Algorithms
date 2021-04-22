"""
_________________________68. Text Justification_________________________
Difficulty: Hard		Likes: 715		Dislikes: 1614		Solution: None
Total Accepted: 139.8K		Total Submission: 503.2K		Acceptance Rate: 27.8%
Tags:  String


Given  an  array  of  words and a width maxWidth, format the text such that each
line has exactly maxWidth characters and is fully (left and right) justified.   
You   should   pack   your   words   in   a   greedy  approach;  that  is,  pack
as   many   words  as  you  can  in  each  line.  Pad  extra  spaces  '  '  when
necessary so that each line has exactly maxWidth characters.                    
Extra  spaces  between  words  should  be  distributed as evenly as possible. If
the  number  of  spaces  on a line do not divide evenly between words, the empty
slots on the left will be assigned more spaces than the slots on the right.     
For    the    last    line    of    text,    it   should   be   left   justified
and no extra space is inserted between words.                                   
Note:                                                                           
																																								
A       word       is       defined       as      a      character      sequence
consisting of non-space characters only.                                        
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.  
The input array words contains at least one word.                               
																																								
																																								


Example 1: 
 Input:
 words = ["This", "is", "an", "example", "of", "text", "justification."]
 maxWidth = 16
 Output:
 [
    "This    is    an",
    "example  of text",
    "justification.  "
 ]
	
Example 2: 
 Input:
 words = ["What","must","be","acknowledgment","shall","be"]
 maxWidth = 16
 Output:
 [
   "What   must   be",
   "acknowledgment  ",
   "shall be        "
 ]
              because the last line must be left-justified instead of fully-justified.
							Note that the second line is also left-justified becase it contains only one word.
	
Example 3: 
 Input:
 words = ["Science","is","what","we","understand","well","enough","to","explain",
          "to","a","computer.","Art","is","everything","else","we","do"]
 maxWidth = 20
 Output:
 [
   "Science  is  what we",
	 "understand      well",
   "enough to explain to",
   "a  computer.  Art is",
   "everything  else  we",
   "do                  "
 ]
	
"""


import functools
import itertools
import operator
import bisect
import array
import collections
from typing import *


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        l = maxWidth
        lengths = [*map(len, words)]
        res = []
        prev = 0
        s = 0
        i = 0
        while i < len(words):
            s += lengths[i] + 1
            if s-1 > l:
                s = (lengths[i] + 1)
                if prev == None:
                    prev = 0
                res.append(words[prev: i])
                prev = i
            i += 1

        res.append(words[prev:])

        t = []
        for i in range(len(res)-1):
            line = res[i]
            if len(line) == 1:
                t.append(' '.join(line).ljust(l))
            else:
                n, r = divmod(l - (sum(map(len, line)) +
                                   len(line)) + 1, len(line) - 1)
                narrow = ' ' * (n + 1)
                if r == 0:
                    t.append(narrow.join(line))
                else:
                    wide = ' ' * (n + 2)
                    t.append(wide.join(line[:r] + [narrow.join(line[r:])]))

        t.append(' '.join(res[-1]).ljust(l))

        return t


if __name__ == "__main__":
    pass


"""
"""
