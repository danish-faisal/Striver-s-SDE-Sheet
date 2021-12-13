# https://leetcode.com/problems/binary-search-tree-iterator/

# next() is O(h) time & overall O(h) memory, hasNext() in O(1) time

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root=root
        self.stack=[]
        self.pushAll(root)

    def next(self) -> int:
        nxt=self.stack.pop()
        self.pushAll(nxt.right)
        return nxt.val
        

    def hasNext(self) -> bool:
        return len(self.stack)>0
        
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node=node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()