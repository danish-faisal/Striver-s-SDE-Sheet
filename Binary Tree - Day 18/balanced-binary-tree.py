# https://leetcode.com/problems/balanced-binary-tree/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Optimal Approach: TC - O(N), SC - O(N)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
                # call the recursive-height-calc helper-func, compare its returned value
        return self.dfsHeight(root)!=-1
    
    def dfsHeight(self, root):
        if root==None:
            return 0

        lh=self.dfsHeight(root.left)    # get the height of left-subtree
        if lh==-1:      # if the left-subtree returns -1, keep returning -1
            return -1
        
        rh=self.dfsHeight(root.right)   # get the height of right-subtree
        if rh==-1:      # if the right-subtree returns -1, keep returning -1
            return -1
        
        if abs(lh-rh)>1: # if the diff b/w lh & rh > 1, return -1
            return -1
        
        return 1+max(lh,rh)     # return height, incase of balanced tree

'''
Brute Force Soln: TC - O(N^2), SC - Auxillary O(N)
At each node, recursively calculate the height of the left-subtree & right-subtree of the node
check if the difference between them is >1, if yes return False
else call this same function again on its left-child-node and right-child-node, return False if any of them returns -1 else return True
'''