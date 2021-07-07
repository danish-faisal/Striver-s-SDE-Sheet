# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        t1 = headA
        t2 = headB
        m=n=0
        # get the length of individual lists
        while t1 or t2:
            if t1:
                m+=1
                t1=t1.next
            if t2:
                n+=1
                t2=t2.next
        t1 = headA
        t2 = headB
        # iterate the list1 by the times it is greater than list2 in length
        if m<n:
            for i in range(n-m):
                t2=t2.next
        # iterate the list2 by the times it is greater than list1 in length
        else:
            for i in range(m-n):
                t1=t1.next
        # start iterating the two lists parallely comparing the nodes
        while t1 and t2:
            if t1 == t2:
                return t1
            t1=t1.next
            t2=t2.next
        return None