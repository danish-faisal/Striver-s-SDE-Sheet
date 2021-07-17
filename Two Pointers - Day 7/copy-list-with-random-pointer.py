# https://leetcode.com/problems/copy-list-with-random-pointer/

# APPROACH 1 - USING HASHMAP

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
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