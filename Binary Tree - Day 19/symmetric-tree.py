# https://leetcode.com/problems/symmetric-tree/

# Optimal Soln: TC - O(N), SC - Auxillary O(N)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
                # symmetric is root is None, else call the recursive-helper-func on left & right subtree
        return root==None or self.isSymmetricHelper(root.left, root.right)
    
    def isSymmetricHelper(self, left, right):
        # if any of the two is None, check if the other one is None as well
        if left==None or right==None:
            return left==right
        
        # assymetric if the values are different
        if left.val!=right.val:
            return False
                # check left-subtree of left-child == right-subtree of right-child for symmetricity
                # check right-subtree of left-chilf == left-subtree of right-child for symmetricity
        return self.isSymmetricHelper(left.left,right.right) and self.isSymmetricHelper(left.right,right.left)