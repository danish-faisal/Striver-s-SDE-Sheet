# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Left, Right, Root

# Iterative:
# Using 1 Stack: TC - O(2N), SC - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postord=[]
        if root==None:
            return postord
        stack=[]
        curr=root
        while curr!=None or len(stack)!=0:      # until stack has nodes or curr is set to a node
            if curr!=None:          # if curr is set to a node
                stack.append(curr)  # push the curr in stack
                curr=curr.left      # update curr to its left node
            # if curr is null
            else:
                temp=stack[-1].right        # get the right-child of top-node in the stack
                if temp==None:                      # if there's no right-child
                    temp=stack.pop()                # pop the top-node
                    postord.append(temp.val)        # append this node to postord-arr
                    
                    # check if the curr-node belongs to a chain of right-nodes and no-left-node
                    # until stack is not empty and nodes on stack form a chain of right-sub-tree
                    while len(stack)!=0 and temp==stack[-1].right:
                        temp=stack.pop()                # pop the top-node in the stack
                        postord.append(temp.val)        # append the node to postord-arr
                
                else:           # if there's a right-child make it the curr-node
                    curr=temp
                    
        return postord

# Using 2 Stacks: TC - O(N), SC - O(2N)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder=[]
        if root==None:
            return postorder
        
        stack1=[root]
        stack2=[]
        
        while len(stack1)!=0:
            node=stack1.pop()           # pop nodes from Stack1 to Stack2, will be popped in order Right-Left-Root
            stack2.append(node.val)     # push in Stack2 in order: Root-Left-Right
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        while len(stack2)!=0:           # as the pushed order in Stack1 is Right-Left-Root => PostOrder
            postorder.append(stack2.pop())
        
        return postorder

# Recursive: TC - O(N), SC - Auxillary O(N)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.recursiveHelper(root, ans)
        return ans
    
    def recursiveHelper(self, root, ans):   # recursively call the function in PostOrder
        if root==None:
            return
        self.recursiveHelper(root.left, ans)
        self.recursiveHelper(root.right, ans)
        ans.append(root.val)