# https://leetcode.com/problems/same-tree/

# Soln: TC - O(N), SC - Auxillary O(N)
# If trees are same/identical their inorder traversal should be same

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if any node is null
        if p==None or q==None:
            return p==q     # check if both are null, or just one node
        
        # check if the ndoes have the same values ad call the same-func recursively on left and right subtrees
        return (p.val==q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)