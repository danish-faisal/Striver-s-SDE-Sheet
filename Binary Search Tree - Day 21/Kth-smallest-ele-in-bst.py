# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Iterative Soln - TC: O(N), SC: O(N)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right