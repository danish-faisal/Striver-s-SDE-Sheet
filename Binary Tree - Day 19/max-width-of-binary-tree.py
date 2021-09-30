# https://leetcode.com/problems/maximum-width-of-binary-tree/

# Optimal Soln: TC - O(N), SC - O(N)
# On each level keep track of no. of node 0->N including missing nodes
# max-width = last_idx - first_idx + 1 on each level

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        
        dq=deque()              # hould use a simple-queue
        dq.append([root,0])
        ans=0
        while len(dq)>0:
            size=len(dq)
            minn=dq[0][1]       # min_idx on a level
            first=last=None
            for i in range(size):
                cur_idx=dq[0][1]-minn           # curr_idx of a node in range (0,max-in-a-level) => mapped_idx - minn
                node=dq[0][0]           # get the node
                dq.popleft()
                if i==0:
                    first=cur_idx       # idx of first node on a level
                if i==size-1:
                    last=cur_idx        # idx of last node on a level
                if node.left:
                    dq.append([node.left, 2*cur_idx+1])     # push the left-child along with its mapped-idx
                if node.right:
                    dq.append([node.right, 2*cur_idx+2])    # push the right-child along with its mapped-idx
                
            ans=max(ans,last-first+1)       # calc max-at this level, compare with the prev-max and get the ans
        
        return ans