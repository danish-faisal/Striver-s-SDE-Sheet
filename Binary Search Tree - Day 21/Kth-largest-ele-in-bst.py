# https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1

# Iterative Soln - TC: O(N), SC: O(N)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.left
        
        return -1