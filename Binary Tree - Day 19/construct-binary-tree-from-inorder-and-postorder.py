# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Optimal Soln: TC - O(N), SC - O(N) + Auxillary O(N)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Hash the nodes-val with their index-val given in inorder 
        inMap={}
        for i in range(len(inorder)):
            inMap[inorder[i]]=i
        
        # call the recursive helper function
        root=self.buildingTree(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,inMap)
        
        return root
    
    def buildingTree(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):
        # when inorder or preorder arrays have exhausted/ checked for both left & right subtrees
        if inStart>inEnd or preStart>preEnd:
            return None
        
        # get the root, first in preorder in the range (preStart, preEnd)
        root=TreeNode(preorder[preStart])
        # get the index of the root in inorder
        inRoot=inMap[root.val]
        # calc no. of nodes to the left of root in range [inStart.....inRoot.....inEnd]
        numsLeft=inRoot-inStart
        
        # for left-subtree, update the range of preorder to (preStart+1, preStart+numsLeft) "to the right of root" 
        # & inorder to (inStart, inRoot-1) "to the left of root"
        root.left=self.buildingTree(preorder,preStart+1,preStart+numsLeft,inorder,inStart,inRoot-1,inMap)

        # for right-subtree, update the range of preorder to (preStart+numsLeft+1, preEnd) "whatever left to the right og numsLeft"
        # & inorder to (inRoot+1, inEnd) "to the right of root"
        root.right=self.buildingTree(preorder,preStart+numsLeft+1,preEnd,inorder,inRoot+1,inEnd,inMap)
        
        return root