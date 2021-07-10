# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        # find collision point -> also proves presence of the cycle
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                break
        # return if no cycle
        if not fast or not fast.next:
            return None
        # initialize the second-ptr to head - while the first-ptr is at collision point
        fast=head
        # traverse both nodes parallely until they meet
        while slow!=fast:
            fast=fast.next
            slow=slow.next
        # the point the meet at - is the cycle-point
        return slow

'''
If there is a cycle, return the entry location of the cycle:
1) L1 is defined as the distance between the head point and entry point
2) L2 is defined as the distance between the entry point and the meeting point
3) C is defined as the length of the cycle
4) n is defined as the travel times of the fast pointer around the cycle When the first encounter of the slow pointer and the fast pointer

According to the definition of L1, L2 and C, we can obtain:

the total distance of the slow pointer traveled when encounter is L1 + L2

the total distance of the fast pointer traveled when encounter is L1 + L2 + n * C

Because the total distance the fast pointer traveled is twice as the slow pointer, Thus:

2 * (L1+L2) = L1 + L2 + n * C => L1 + L2 = n * C => L1 = (n - 1) C + (C - L2)*

It can be concluded that the distance between the head location and entry location is equal to the distance between the meeting location and the entry location along the direction of forward movement.

So, when the slow pointer and the fast pointer encounter in the cycle, we can define a pointer "entry" that point to the head, this "entry" pointer moves one step each time so as the slow pointer. When this "entry" pointer and the slow pointer both point to the same location, this location is the node where the cycle begins.
'''