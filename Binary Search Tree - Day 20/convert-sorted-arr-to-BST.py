# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Recursive Soln: TC - O(N), SC - Auxillary O(N)

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        return self.constructFromArray(nums,0,len(nums)-1)
    
    def constructFromArray(self,nums,left,right):
        if left>right:
            return None
        mid=(left+right)//2
        node=TreeNode(nums[mid])
        
        node.left=self.constructFromArray(nums,left,mid-1)
        node.right=self.constructFromArray(nums,mid+1,right)
        
        return node