# https://www.geeksforgeeks.org/bottom-view-binary-tree/
# https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

# Iterative: TC - O(N), SC - O(2N)

from sortedcontainers import SortedDict
from collections import deque

class Solution:
    def bottomView(self, root):
        ans=[]
        if root==None:
            return ans
        # sorted-dict/ordered map => keeps all the keys in sorted-order
        sdict=SortedDict()      # can also use dict, but need to again use "sorted(dict.keys())" to append in correct order 

        dq=deque()              # for pop-from-front, O(1) operation

        dq.append([root,0])     # Parallel lines concept, line=0 for root, -1 as we moe left, +1 as we move right
                                # also for overlapping nodes, right node is considered to be seen from bottom-view
                                # like right-node of level-1 node of left-sub-tree and left-node of same-level node from right-sub-tree

        while len(dq)!=0:       # until the deque is not empty 
            node=dq.popleft()   # get the pair of (node, line) at front of queue
            line=node[1]        # store the value of line at current-node 
            sdict[line]=node[0].val     # add/update the latest-value of the node seen as we move into lower-levels 

            if node[0].left:    # append the left-child of curr-node if exists, to the queue 
                dq.append([node[0].left,line-1])
            if node[0].right:   # append the right-child of curr-node if exists to the queue
                dq.append([node[0].right,line+1])
        
        for a in sdict:         # append the values in left-to-right order, which will be in sorted form as keys are ...-2,-1,0,1,2,....
            ans.append(sdict[a])

        return ans


# for Recursive Solution: need to use extra logic, to keep account of height along with the lines to update a node
# as In reursive inorder traversal is used, the nodes in the right-sub-tree of upper-level will be visited after the nodes in left-sub-tree for lower-level