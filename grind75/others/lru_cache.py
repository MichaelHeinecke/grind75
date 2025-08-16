from typing import Hashable, Any


class Node:
    def __init__(self, prev, nxt, key, value):
        self.prev = prev
        self.nxt = nxt
        self.key = key
        self.value = value


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None, None, None)
        self.tail = Node(None, None, None, None)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def __len__(self):
        return len(self.cache)

    def __contains__(self, key):
        return key in self.cache

    def put(self, key: Hashable, value: Any):
        if key not in self.cache:
            # Insert key value pair in cache and prepend to doubly linked list
            node = Node(self.head, self.head.nxt, key, value)
            self.cache[key] = node
            self.head.nxt.prev = node
            self.head.nxt = node

            if len(self.cache) > self.capacity:
                # Evict LRU element
                lru = self.tail.prev
                self.cache.pop(lru.key)
                # Remove from end of doubly linked list
                lru.prev.nxt = self.tail
                self.tail.prev = lru.prev
        else:
            node = self.cache[key]
            node.value = value
            # Move key value pair to front of doubly linked list
            # Remove node
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev
            # Prepend at front
            node.nxt = self.head.nxt
            node.prev = self.head
            self.head.nxt.prev = node
            self.head.nxt = node

    def get(self, key):
        # If key exists, move element at front of doubly linked list and return value
        if key in self.cache:
            node = self.cache[key]
            # Remove node
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev
            # Prepend at front
            node.nxt = self.head.nxt
            node.prev = self.head
            self.head.nxt.prev = node
            self.head.nxt = node
            return self.cache[key].value
        else:
            return -1
