# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Time complexity: O(N) where n is the number of nodes.
# Space complexity: O(N), auxiliary space.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None or root==p or root==q:
            return root
        
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        
        if left==None:
            return right
        elif right==None:
            return left
        else:
            return root