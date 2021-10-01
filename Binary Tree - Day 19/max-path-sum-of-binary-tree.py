# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Optimal Soln: TC - O(N), SC - Auxillary O(N)

class Solution:
    maxi=-2147483648        # static-var to store the max-result
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximumPathSum(root)
        return self.maxi
    
    def maximumPathSum(self, root):
        if root==None:      # Base Case
            return 0
        # leftSum & rightSum store max-path-sum going through left and right child of root respectively
        leftSum=max(0, self.maximumPathSum(root.left))      # compare with 0, to ignore negative values because in case of negative values
        rightSum=max(0, self.maximumPathSum(root.right))    # considering value of only root will obviously be greater
        
        self.maxi=max(self.maxi, root.val+leftSum+rightSum)     # compare this subtree's sum value with any other prev-assgined-max and update
        
        return root.val+max(leftSum, rightSum)          # return the max-path-sum obtained from this subtree