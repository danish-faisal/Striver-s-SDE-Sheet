# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Optimal Soln: TC - O(N) [+ logn in some cases for HashMap], SC - O(N) + Auxillary O(N)

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Hash the nodes-val with their index-val given in inorder
        inMap={}
        for i in range(len(inorder)):
            inMap[inorder[i]]=i
        
        # call the recursive helper function
        root=self.buildingTree(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1,inMap)
        
        return root
    
    def buildingTree(self,inorder,inStart,inEnd,postorder,postStart,postEnd,inMap):
        # when inorder or postorder arrays have exhausted/ checked for both left & right subtrees
        if inStart>inEnd or postStart>postEnd:
            return None
        
        # get the root, first in postorder in the range (postStart, postEnd)
        root=TreeNode(postorder[postEnd])
        # get the index of the root in inorder
        inRoot=inMap[root.val]
        # calc no. of nodes to the left of root in range [inStart.....inRoot.....inEnd]
        numsLeft=inRoot-inStart
        
        # for left-subtree, update the range of postorder to (postStart, postStart+numsLeft-1) "to the left of right-subtree nodes & root" 
        # & inorder to (inStart, inRoot-1) "to the left of root"
        root.left=self.buildingTree(inorder,inStart,inRoot-1,postorder,postStart,postStart+numsLeft-1,inMap)
        
        # for right-subtree, update the range of postorder to (postStart+numsLeft, postEnd-1) "whatever left to the right of numsLeft - Root"
        # & inorder to (inRoot+1, inEnd) "to the right of root"
        root.right=self.buildingTree(inorder,inRoot+1,inEnd,postorder,postStart+numsLeft,postEnd-1,inMap)
        
        return root