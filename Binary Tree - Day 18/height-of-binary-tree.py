# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Soln: TC - O(N), SC - Auxillary O(N)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        # Compute the depth of each subtree
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)
                    # Use the larger one
        return 1 + max(lh, rh)


# Iterative Soln: TC - O(N), SC - O(N)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        
        dq=deque()          # should use a simple queue
        dq.append(root)
        nodeCount=0         # to keep the count of nodes at curr-level
        height=0
        
        while True:
            nodeCount=len(dq)       # get the no. of nodes at curr-level
            if nodeCount==0:        # if dq is empty means we've gone to the depth in the prev-iteration
                return height       # so return the height
            else:
                height+=1           # increase the height, if the curr-level has nodes
            
            while nodeCount>0:          # pop the nodes of curr-level out of queue, and push in their child-nodes
                node=dq.popleft()       # popping out front-node from the Queue
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                nodeCount-=1