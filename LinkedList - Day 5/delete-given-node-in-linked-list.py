# https://leetcode.com/problems/delete-node-in-a-linked-list/

'''Write a function to delete a node in a singly-linked list. 
You will not be given access to the head of the list, 
instead you will be given access to the node to be deleted directly.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # get the val of next-node in the node-to-be-deleted
        node.val = node.next.val
        # get the next-ptr of the next-node in the next-ptr of the node-to-be-deleted
        node.next = node.next.next