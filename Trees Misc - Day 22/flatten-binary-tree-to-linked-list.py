# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Iterative Approach 2: TC - O(N), SC - O(1)
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root==None:
            return
        curr=root
        
        while curr!=None:
            if curr.left!=None:
                prev=curr.left
                while prev.right:
                    prev=prev.right
                prev.right=curr.right
                curr.right=curr.left
                curr.left=None
            curr=curr.right

# Iterative Approach 1: TC - O(N), SC - O(N)
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root==None:
            return
        stack=[root]
        
        while len(stack)>0:
            curr=stack.pop()
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            
            if len(stack)!=0:
                curr.right=stack[-1]
            curr.left=None

# Recursive Soln: TC - O(N), SC - O(N)
class Solution:
    prev=None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """ Do not return anything, modify root in-place instead. """
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right=self.prev
        root.left=None
        
        self.prev=root