# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 2 ptrs -> fast and slow
        slow=fast=head
        
        # move faster pointer ahead by n times
        for i in range(n):
            fast=fast.next
        
        # if fast-ptr reaches end -> 1st node is deleted, make head point to 2nd node and return
        if not fast:
            return head.next
        
        # move slow-ptr until fast-ptr reaches the end -> as slow-ptr should stop before the nth-node from the last
        while fast.next!=None:
            fast=fast.next
            slow=slow.next
        
        # point (n-1)th node to (n+1)th node
        slow.next=slow.next.next
        
        return head