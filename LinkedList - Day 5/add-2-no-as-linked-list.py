# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # variable to store the carry
        carry = 0
        # head-ptr of the new result-list
        res = temp = ListNode(0)
        # until list1 or list2 ends or no-carry
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            carry, val = divmod(v1+v2+carry, 10) # -> (x/y,x%y) | x/y will be 0 or 1 in this case & x%y value to be as node
            # create new node with sum obtained by adding 2 nodes of the lists and attach it to the result-list
            temp.next = ListNode(val)
            # incr the ptr in result-list
            temp = temp.next
        return res.next