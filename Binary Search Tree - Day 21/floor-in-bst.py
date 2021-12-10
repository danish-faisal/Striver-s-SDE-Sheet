# https://www.geeksforgeeks.org/floor-in-binary-search-tree-bst/
# https://youtu.be/xm_W1ub-K-w

class Solution:
    def floorInBST(self, root, key):
        floor=-1

        while root:
            if root.val==key:
                floor=root.val
                break
            elif root.val<key:
                floor=root.val
                root=root.right
            else:
                root=root.left
        
        return floor