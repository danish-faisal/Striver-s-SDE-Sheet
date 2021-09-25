# https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/
# https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1

# Iterative Approach: TC - O(N), SC - O(2N)

from sortedcontainers import SortedDict
from collections import deque

class Solution:
    def topView(self,root):
        ans=[]
        
        if root==None:
            return ans
        # sorted-dict/ordered map => keeps all the keys in sorted-order
        sdict=SortedDict()          # can also use dict, but need to again use "sorted(dict.keys())" to append in correct order

        dq=deque()                  # for pop-from-front, O(1) operation
        dq.append([root,0])         # Parallel lines concept, line=0 for root, -1 as we moe left, +1 as we move right
                                    # also for overlapping nodes, right node is considered to be seen from bottom-view
                                    # like right-node of level-1 node of left-sub-tree and left-node of same-level node from right-sub-tree
        
        while len(dq)!=0:
            node=dq.popleft()       # get the pair of (node, line) at front of queue

            if node[1] not in sdict:        # add the value of the node seen as we move into newer-levels
                sdict[node[1]]=node[0].data
            
            if node[0].left:
                dq.append([node[0].left,node[1]-1])
            if node[0].right:
                dq.append([node[0].right,node[1]+1])
        
        for i in sdict:             # append the values in left-to-right order, which will be in sorted form as keys are ...-2,-1,0,1,2,....
            ans.append(sdict[i])
        
        return ans

# Recursive Approach: need to use extra logic, to keep account of height along with the lines to update a node
# as In recursive inorder traversal is used, the nodes in the right-sub-tree of upper-level will be visited after the nodes in left-sub-tree for lower-level