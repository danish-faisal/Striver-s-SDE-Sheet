# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# TC - O(N), SC - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if root==None:
            return ans
        dq=Deque()          # should use a simple queue
        dq.append(root)
        lToR=True           # flag to track when to go Left-To-right & when Right-To-Left
        
        while len(dq)>0:
            n=len(dq)       # curr-len of the Queue
            row=[-1 for x in range(n)]      # Array of size 'n', to store the node of curr-level 
            
            for i in range(n):      # for each nod ein the curr-level
                node=dq.popleft()
                # if flag is set, order is L-to-R else R-to-L
                pos=i if lToR else n-i-1
                
                row[pos]=node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
            lToR=not lToR       # change the order on completion of a level
            ans.append(row)
        
        return ans