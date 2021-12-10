# https://www.geeksforgeeks.org/floor-and-ceil-from-a-bst/
# https://youtu.be/KSsk8AhdOZA

# TC: O(N), SC: O(1)

class Solution:
    def ceilInBST(self, root, key):
        ceil=-1

        while root:
            if root.val==key:
                ceil=root.val
                break
            elif root.val<key:
                root=root.right
            else:
                ceil=root.val
                root=root.left
        
        return ceil