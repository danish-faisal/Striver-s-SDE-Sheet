# https://leetcode.com/problems/validate-binary-search-tree/

# Recursive Optimal Soln: TC - O(N), SC - Auxillary O(N)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBT(root, None, None)
    
    def checkBT(self,root, mx, mn):
        if root==None:
            return True
        if mx!=None and root.val>=mx:
            return False
        if mn!=None and root.val<=mn:
            return False
        
        return self.checkBT(root.left,root.val,mn) and self.checkBT(root.right,mx,root.val)