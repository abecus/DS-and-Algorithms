"""
_________________________146. LRU Cache_________________________
Difficulty: Medium		Likes: 6575		Dislikes: 280		Solution: Available
Total Accepted: 605.1K		Total Submission: 1.8M		Acceptance Rate: 33.7%
Tags:  Design


Design        a        data        structure        that       follows       the
constraints of a Least Recently Used (LRU) cache.                               
Implement the LRUCache class:                                                   
                                                                                
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.    
int       get(int       key)       Return       the       value      of      the
key if the key exists, otherwise return -1.                                     
void  put(int  key,  int  value) Update  the value of the key if the key exists.
Otherwise,  add  the  key-value  pair  to  the  cache.  If  the  number  of keys
exceeds the capacity from this operation, evict the least recently used key.    
                                                                                
Follow up:                                                                      
Could you do get and put in O(1) time complexity?                               
                                                                                
                                                                                


Example 1:  Input
 ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"] [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]] Output
 [null, null, null, 1, null, -1, null, -1, 3, 4]  Explanation
 LRUCache lRUCache = new LRUCache(2);
 lRUCache.put(1, 1); // cache is {1=1} lRUCache.put(2, 2); // cache is {1=1, 2=2} lRUCache.get(1);    // return 1 lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3} lRUCache.get(2);    // returns -1 (not found) lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3} lRUCache.get(1);    // return -1 (not found) lRUCache.get(3);    // return 3 lRUCache.get(4);    // return 4     1 <= capacity <= 3000 0 <= key <= 3000 0 <= value <= 104 At most 3 * 104 calls will be made to get and put.
  
"""


import functools, itertools, operator, bisect, array, collections 
from typing import * 

class LRUCache:

    def __init__(self, capacity: int):
        

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == "__main__":
	pass


"""
similarQuestions::
		LFU Cache: Hard
		Design In-Memory File System: Hard
		Design Compressed String Iterator: Easy
"""
