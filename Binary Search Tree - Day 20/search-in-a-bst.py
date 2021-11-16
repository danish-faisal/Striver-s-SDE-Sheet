# https://leetcode.com/problems/search-in-a-binary-search-tree/

# Iterative Soln: TC - O(logN), SC - O(1)

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return None
        
        temp=root
        
        while temp is not None:
            if temp.val==val:
                return temp
            elif val<temp.val:
                temp=temp.left
            else:
                temp=temp.right
        
        return None