class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        node = self.d[key]
        self.removeFromList(node)
        self.addHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.removeFromList(node)
            self.addHead(node)
        else:
            node = Node(key, value)
            self.d[key] = node
            self.addHead(node)
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.removeFromTail()

    def addHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def removeFromTail(self):
        if not len(self.d): return 
        node = self.tail.prev
        self.d.pop(node.key)
        self.removeFromList(node)
        

