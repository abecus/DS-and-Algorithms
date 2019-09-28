"""
You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order and each of their 
nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        s = head
        c=0
        
        while l1 or l2:
            if l1 and l2:
                t = l1.val+l2.val+c
                if t>9:
                    c=1
                    t-=10
                else:
                    c=0
                temp = ListNode(t)
                s.next = temp
                s = s.next
                l2 = l2.next
                l1 = l1.next
            
            elif l1:
                t = l1.val+c
                if t>9:
                    c=1
                    t-=10
                else:
                    c=0
                temp = ListNode(t)
                s.next = temp
                s = s.next
                l1 = l1.next
                
            elif l2:
                t = l2.val+c
                if t>9:
                    c=1
                    t-=10
                else:
                    c=0
                temp = ListNode(t)
                s.next = temp
                s = s.next
                l2 = l2.next
        if c:
            s.next = ListNode(c)
        
        return head.next
        
            
            
     