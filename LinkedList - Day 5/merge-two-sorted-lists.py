# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if no List1 return List2
        if l1 is None: return l2
        # if no Lost 2 return List 1
        if l2 is None: return l1
        
        # head node of the new linked list we're creating by merging the other two
        dummy=temp=ListNode()
        
        # while anyone of the List's reaches end
        while l1!=None and l2!=None:
            # if value at List 1 is lower
            if l1.val<=l2.val:
                # L1's node will come before the L2's node while merging
                temp.next=l1
                # move ahead to the next node in L1 for comparision
                l1=l1.next
            else:
                temp.next=l2
                l2=l2.next

            temp=temp.next
        # after anyone of the List's end -> the merged list will point to the List that have few nodes remaining
        temp.next = l1 or l2
        
        return dummy.next