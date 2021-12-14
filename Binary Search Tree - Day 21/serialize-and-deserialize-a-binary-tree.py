# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

'''
time complexity and space complexity are O(n).
Time complexity is O(n) since it has to traverse through all nodes.
Space complexity is O(n) since the recursive stack may go up to n, in case the tree is completely skewed.
'''

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def doIt(node):
            if node:
                vals.append(str(node.val))
                doIt(node.left)
                doIt(node.right)
            else:
                vals.append('#')
        vals=[]
        doIt(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def doIt():
            val=next(vals)
            if val=='#':
                return None
            else:
                node=TreeNode(int(val))
                node.left=doIt()
                node.right=doIt()
                return node
        vals=iter(data.split())
        return doIt()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))