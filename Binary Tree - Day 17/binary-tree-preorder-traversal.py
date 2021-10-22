# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Iterative: TC - O(N), SC - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder=[]
        if root==None:  # if root is null
            return preorder
        
        stack=[root]    # stack to keep track of the nodes traversed
        
        while len(stack)!=0:
            node=stack.pop()                # take the node at top-of-the-stack
            preorder.append(node.val)       # print its val
            if node.right:                  # append its right to stack, 1st right as stack is LIFO
                stack.append(node.right)    # so to travel Left first, it should be pushed at last
            if node.left:                   # append its left to stack
                stack.append(node.left)
        
        return preorder

# Recursive: TC : O(N), SC : Auxillary O(N)

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.recursiveHelper(root,ans)
        return ans
    
    def recursiveHelper(self,root,ans):
        if root==None:
            return
        ans.append(root.val)
        self.recursiveHelper(root.left,ans)
        self.recursiveHelper(root.right,ans)
    