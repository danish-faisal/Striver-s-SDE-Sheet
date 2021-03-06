# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Morris Traversal: TC - O(N), SC - O(1)
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # Do not return anything, modify root in-place instead.
        if root==None:
            return
        
        curr=root
        while curr!=None:
            if curr.left!=None:
                prev=curr.left
                while prev.right:       # go to right-most-leaf-node in left-subtree
                    prev=prev.right
                prev.right = curr.right     # point the rightmost-leftnode to right-subtree
                curr.right=curr.left        # make the node's left-subtree move-to right
                curr.left=None              # make the node's left-subtree to null
            curr=curr.right     # move to next-node in the line

# Iterative Soln: TC - O(N), SC - O(N)
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # Do not return anything, modify root in-place instead.
        if root==None:
            return
        stack=[root]
        while len(stack)>0:         # until the stack is emptied
            curr=stack.pop()
            if curr.right:              # append the right-child of curr to stack
                stack.append(curr.right)
            if curr.left:               # append the left-child of curr to stack
                stack.append(curr.left)
            
            if len(stack)>0:
                curr.right=stack[-1]    # make the top-node in the stack, right-child of curr-node
            
            curr.left=None      # make the left-child of curr-node point to Null


# Recursive Soln: TC - O(N), SC - O(N)
class Solution:
    prev=None
    def flatten(self, root: Optional[TreeNode]) -> None:
        # Do not return anything, modify root in-place instead.
        if root==None:
            return
        # Going in Right-Left-Root order
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right=self.prev        # as prev stores the prev-traversed-node
        root.left=None
        
        self.prev=root          # update prev to curr-node