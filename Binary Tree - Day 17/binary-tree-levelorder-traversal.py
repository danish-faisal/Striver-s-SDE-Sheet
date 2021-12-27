# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Recursive Soln: TC - O(N), SC - Auxillary O(H)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        self.level(root, res, 1)
        return res
    
    def level(self, root, res, level):
        if not root:
            return
        if level>len(res):
            res.append([root.val])
        else:
            res[level-1].append(root.val)
        self.level(root.left, res, level+1)
        self.level(root.right, res, level+1)

# Iterative Soln: TC - O(N), SC - O(N)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        s=[root]
        res=[]
        while len(s)>0:
            n=len(s)
            lvl=[]
            while n>0:
                node=s.pop(0)
                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)
                lvl.append(node.val)
                n-=1
            res.append(lvl)
        
        return res