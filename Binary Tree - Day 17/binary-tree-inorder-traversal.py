# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Left - Root - Right

# Iterative: TC - O(N), SC - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # similar to the auxillary stack-space used in recursion by the system, we use our own stack to keep track of the nodes
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        inorder=[]
        node=root
        
        while True:
            if node!=None:
                stack.append(node)  # append every node travaersed until a leaf node is reached
                node=node.left      # update the left of curr-node to be the node for next-iteration
            else:
                if len(stack)==0:   # all nodes are checked, so break out of the loop
                    break
                node=stack.pop()    # if a node is reached whose left-sub is checked, pop it out of stack
                inorder.append(node.val)    # print the node's val
                node=node.right     # update the node in the next-iteration to be curr-node's right
        
        return inorder

# Recursive: TC - O(N), SC - Auxillary O(N)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.recursiveHelper(root,ans)
        return ans
   
    def recursiveHelper(self, root, ans):
        if root==None:
            return
        self.recursiveHelper(root.left, ans)
        ans.append(root.val)
        self.recursiveHelper(root.right, ans)
    