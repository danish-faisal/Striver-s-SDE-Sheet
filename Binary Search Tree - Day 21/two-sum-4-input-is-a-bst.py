# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Recursive Soln: TC - O(N), SC - O(N) for Hashmap & O(N) for Stack space

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ht={}
        self.helper(root, ht, k)
        
        for v in ht:
            if ht[v]:
                return True
        
        return False
    
    def helper(self, root, ht, k):
        if root==None or root==k:
            return False
        
        temp=k - root.val
        if temp in ht:
            ht[temp]=True
        else:
            ht[root.val]=False
        
        self.helper(root.left, ht, k)
        self.helper(root.right, ht, k)