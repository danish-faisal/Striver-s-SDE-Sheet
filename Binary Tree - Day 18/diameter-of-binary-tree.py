# https://leetcode.com/problems/diameter-of-binary-tree/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Optimal Approach: TC - O(N), SC - O(N)

class Solution:
    maxdia=0        # static variable, to store the max-diameter seen in the tree

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.recursiveHelper(root, self.maxdia)     # call the recursive solution helper function
        return self.maxdia
    
    # Add an extra logic to keep track of the max-diameter seen, while getting the height of the tree
    def recursiveHelper(self, root, maxdia):
        if root==None:
            return 0
        # get the height of left-sub-tree
        lh = self.recursiveHelper(root.left, maxdia)
        # get the height of right-sub-tree
        rh = self.recursiveHelper(root.right, maxdia)
        # lh+rh => max-diameter seen between 2 leaf-nodes of the sub-tree
        # update the max-diameter
        self.maxdia=max(self.maxdia, lh+rh)

        # return height
        return 1+max(lh,rh)

# Brute Force soln: Calculate the height from each node in the tree as lh+rh = max-diameter
# keep track of diameters previously seen and check on each node with curr-diameter seen to update max-diameter with the greater one

# TC - O(N^2), SC - Auxillary O(N)