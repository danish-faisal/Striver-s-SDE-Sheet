# https://leetcode.com/problems/binary-tree-right-side-view/

# Recursive Approach: TC - O(N), SC - Auxillary O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ds=[]
        self.recursiveHelper(root, 0, ds)
        return ds
    
    def recursiveHelper(self, root, level, ds):
        if root==None:
            return
        
        if level==len(ds):          # push into the ds-array if curr-level == curr-sze of ds/no. of nodes in ds
            ds.append(root.val)     # as this indicates that we have entered a new level
        
        self.recursiveHelper(root.left, level+1, ds)        # left first => level-order traversal from left-size to get the left-view
        self.recursiveHelper(root.right, level+1, ds)