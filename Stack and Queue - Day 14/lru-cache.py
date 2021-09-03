# https://leetcode.com/problems/lru-cache/

# TC: O(1), SC: O(N)

class Node:     # Node class for Doubly Linked List
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        # cache-capacity
        self.capacity = capacity
        # dictionary for hashing key:value pairs
        self.dic = dict()
        # head & tail of the DoublyLinkedList Cache
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        # if the passed key is in our dictionary of cached-elements
        if key in self.dic:
            # get the node from the dic
            n = self.dic[key]
            # remove it from the DLL
            self._remove(n)
            # Add it to the DLL again at front as it will now change to Most-Recently-Used
            self._add(n)
            # return its value
            return n.val
        # return -1 if its not in our cache
        return -1

    def put(self, key, value):
        # check if a node with same key exists
        if key in self.dic:
            # yes: remove it from the DLL
            self._remove(self.dic[key])
        # create a new node with the passed (key,val)
        n = Node(key, value)
        # add it to the front of the DLL as MRU
        self._add(n)
        # hash the node with the key in the dic
        self.dic[key] = n
        # if cache capacity overflows
        if len(self.dic) > self.capacity:
            # get the LRU from the DLL's tail
            n = self.tail.prev
            # remove it
            self._remove(n)
            # del it from the dic
            del self.dic[n.key]

    def _remove(self, node):
        # get the node before the curr-node to be del
        p = node.prev
        # get the node after the curr-node to be del
        n = node.next
        # link curr-node' prev to curr-node's next & vice versa
        p.next = n
        n.prev = p

    # add any new node to the front of DLL
    def _add(self, node):
        # get the node next to head
        n = self.head.next
        # make that node's prev point to new-node
        n.prev = node
        # made new-node the next node to head
        self.head.next = node
        # new-node's next will be the prev-node pointed by head.next
        node.next = n
        # new-node's prev node will be node at head
        node.prev = self.head
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)