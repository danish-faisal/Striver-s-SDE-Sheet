# https://leetcode.com/problems/copy-list-with-random-pointer/

# APPROACH 2 - Two Pointers
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        temp=head
        # create copy-nodes of the same value as org-node and have the copy-node as the next-node of the org-node
        while temp:
            nxt=temp.next
            new=Node(temp.val)
            temp.next=new
            new.next=nxt
            temp=temp.next.next
        # initialize temp to head and sec to first copied-node
        temp=head
        sec=temp.next
        # while traversing the list, arrange the random pointers by 
        # make the copied-node random-ptr point to the next-node of the random-node pointed by org-node
        while temp:
            sec.random=temp.random.next if temp.random else None
            sec=sec.next.next if sec.next else None
            temp=temp.next.next
        temp=head
        # have sec as head-ptr to the copied-list
        sec=cur=temp.next
        # arrange the next-ptr correctly of both the lists
        while temp:
            # get the next-node in copied-list
            snxt=cur.next.next if cur.next else None
            # make curr-org-node point to next-org-node
            temp.next=cur.next
            # point first-copied-node to next-copied-node
            cur.next=snxt
            # move to next-node in org-list
            temp=temp.next
            # move to next-node in copied-list
            cur=cur.next
        return sec

# APPROACH 1 - USING HASHMAP

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        copy={}
        # hack to escape from KeyError
        copy[None]=None
        dummy=Node(0)
        dummy.next=head
        temp=dummy.next
        # create new-nodes while traversing the list using the Org-List's node's value
        # and hash them with Org-Node as the Key and New-Copied-Node as the Value
        while temp:
            copy[temp]=Node(temp.val)
            temp=temp.next
        # initialize the dummy-node back to Head
        temp=head
        # while traversing the Org-List again
        # Access the Copy-Node using Org-Node's hash-value and make it's next and random ptr
        # point to new-copied-nodes using the hash-value of the Next-Node and Next-Random-Node in Org-List
        while temp:
            copy[temp].next=copy[temp.next]
            copy[temp].random=copy[temp.random]
            temp=temp.next
        
        # return the hash-value/copied-node of the head as the Head of the copied-list
        newHead=copy[head]
        return newHead