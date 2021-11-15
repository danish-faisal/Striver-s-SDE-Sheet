# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# My Soln: TC - O(N^2), SC - O(N)

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        level=[]
        
        if root==None:
            return None
        
        level.append(root)
        
        while len(level)>0:
            n=len(level)
            
            for i in range(0,n):
                if i<n-1:
                    level[i].next=level[i+1]
                if level[i].left:                
                    level.append(level[i].left)
                if level[i].right:
                    level.append(level[i].right)
            
            level[n-1].next=None
            
            while n>0:
                level.pop(0)
                n-=1
        
        return root