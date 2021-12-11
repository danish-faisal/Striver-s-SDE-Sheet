# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Iterative Solution
# Time complexity: O(H) where H is the height of the tree.
# Space complexity: O(1)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node=root
        
        while node:
            if node.val>p.val and node.val>q.val:
                node=node.left
                continue
            if node.val<p.val and node.val<q.val:
                node=node.right
                continue
            
            return node

# Recursive Solution
# Time complexity: O(H) where H is the height of the tree.
# Space complexity: O(N), Auxillary space

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None:
            return root
        
        if root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        if root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return root