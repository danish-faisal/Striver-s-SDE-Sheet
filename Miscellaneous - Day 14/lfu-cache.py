# https://leetcode.com/problems/lfu-cache/

import collections

class Node:     # Node of DLL
    def __init__(self, key, val):
        self.key = key
        self.val = val
        # curr-freq of the node 
        self.freq = 1
        self.prev = self.next = None

class DLinkedList:      # DLL class with helper funcs
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev=self.head
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def append(self, node):     # add new-node to front 
        # get the existing-node at front
        n=self.head.next
        # get the node pointed by existing-node's prev (basically head)
        p=n.prev
        # new-node's next -> existing-node
        node.next = n
        # new-node's prev -> existing-node's prev
        node.prev = p
        # existing-node's prev -> new-node
        node.next.prev = node
        # existing node's prev's next -> new-node
        node.prev.next = node

        self._size += 1
    
    def pop(self, node=None):       # pop the node at last
        if self._size == 0:
            return
        # if node to delete is not passed => means we're deleting the LRU which'll be at the last of DLL (case of all-nodes with same freq)
        if not node:
            node = self.tail.prev
        # node before last node -> last node's next
        node.prev.next = node.next
        # node after last node -> last node's prev
        node.next.prev = node.prev
        self._size -= 1
        
        return node
        
class LFUCache:
    def __init__(self, capacity):
        # curr-size of cache
        self._size = 0
        # max-size of cache
        self._capacity = capacity
        # Hashmap storing the key: Node
        self._node = dict()
        # Hashmap storing DLL's of diff-freqs
        self._freq = collections.defaultdict(DLinkedList)
        # curr min-freq of all the nodes combined
        self._minfreq = 0
        
        
    def _update(self, node):
        # get the freq of curr-node, to check in the DLL of this freq
        freq = node.freq
        # get the LFU node from that DLL
        self._freq[freq].pop(node)
        # if old DlinkedList has size 0 and self._minfreq is `f`, update self._minfreq to `f+1`
        if self._minfreq == freq and not self._freq[freq]:
            self._minfreq += 1
        # incr curr-node's freq
        node.freq += 1
        # get the new-freq of the curr-node
        freq = node.freq
        # insert the ndoe in new-freq DLL
        self._freq[freq].append(node)
    
    def get(self, key):
        # if node with this key doesn't exist, return -1
        if key not in self._node:
            return -1
        # get the node from _node Hashmap
        node = self._node[key]
        # update its freq
        self._update(node)
        # return its val
        return node.val

    def put(self, key, value):
        # if max-cap itself is 0, nothing can be done
        if self._capacity == 0:
            return
        # if node with the given key exists
        if key in self._node:
            # get the node from _node HM
            node = self._node[key]
            # update its freq
            self._update(node)
            # update its val
            node.val = value
        else:
            # if max-cap is reached
            if self._size == self._capacity:
                # get the LFU node
                node = self._freq[self._minfreq].pop()
                # del the node
                del self._node[node.key]
                # decr the curr-size of cache
                self._size -= 1
            # create new node with the given (key, value)
            node = Node(key, value)
            # hash it
            self._node[key] = node
            # insert it in freq HM with DLL of freq=1
            self._freq[1].append(node)
            # new min-freq = 1, as new-node is inserted
            self._minfreq = 1
            # incr the cache's curr-size
            self._size += 1