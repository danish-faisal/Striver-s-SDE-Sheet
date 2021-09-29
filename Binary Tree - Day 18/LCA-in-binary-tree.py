# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Optimal Soln: Using Recursion - Inorder Traversal; TC - O(N), SC - Auxillary O(N)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If either n1 or n2 matches with root's key, report the presence by returning root
        # (Note that if a key is ancestor of other, then the ancestor key becomes LCA)
        if root==None or root==p or root==q:
            return root
        
        # Look for keys in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left==None:
            return right            # if left is None, return right even if its None
        elif right==None:
            return left             # if left is not None and right is None, we have a node in left-subtree
        else:
            return root             # if both are not None, we got a common-ancestor

'''
Brute Force Soln: TC - O(2N), SC - O(2N)
First, traverse to first node in the given pair and store its path
Then, traverse to second node in the given pair and store its path
Then compare the nodes in the stored paths to find the last common node
'''