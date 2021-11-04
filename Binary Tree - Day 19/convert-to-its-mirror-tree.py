# https://practice.geeksforgeeks.org/problems/mirror-tree/1


class Solution:
    def convertToMirror(self, root):
        if root==None:
            return
        
        self.convertToMirror(root.left)     # traverse each node in left-subtree
        self.convertToMirror(root.right)    # traverse each node in right-subtree

        # swap left & right nodes
        temp = root.left
        root.left = root.right
        root.right = temp