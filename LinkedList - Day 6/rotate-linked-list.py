# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k==0 or head==None:
            return head
        f=head
        n=0
        # find length of the linked-list
        while f:
            f=f.next
            n+=1
        if k>=n:
            k=k%n
        if k==0:
            return head
        f=s=head
        # move first-ptr by k-times
        for i in range(k):
            f=f.next
        # now move first-ptr & second-ptr parallelly -> as first-ptr reaches end, second-ptr will be at (n-k)th node
        # makes virtual division of 0-k nodes LL and (n-k)-n nodes LL
        while f.next:
            f=f.next
            s=s.next
        # point the end of second-half of LL to head
        f.next=head
        # store the starting point of second-half LL -> this will be new head
        newHead=s.next
        # make the end of first-half point to Nothing/None
        s.next=None
        return newHead