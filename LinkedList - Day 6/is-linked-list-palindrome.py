# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        dummy = ListNode()
        dummy.next = head
        fast = slow = dummy
        count = 0
        # find the middle of the Linked List
        while fast and fast.next:
            count+=1
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half of the Linked List
        # second-half identified by mid-node
        # slow is the ptr to reversed second-half
        slow = self.reverseList(slow.next)
        
        # compare corresponding nodes of each half
        while slow:
            dummy=dummy.next
            if dummy.val!=slow.val:
                return False
            slow=slow.next
            
        return True
    
    def reverseList(self,head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next=prev
            prev = curr
            curr = nextTemp
        return prev