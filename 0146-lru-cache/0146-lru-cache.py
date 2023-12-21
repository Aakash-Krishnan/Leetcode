class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = self.tail = None
        self.length = 0
    
    def getHead(self):
        return self.head

    def getLength(self):
        return self.length

    def getKey(self, node):
        return node.key
    
    def getData(self, node):
        return node.val

    def addData(self, data, key):
        newNode = Node(data, key)
        if not self.head:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = self.tail.next

        self.length += 1 

        return newNode
    
    def addNode(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        
        self.length += 1

        return node
    
    def deleteNode(self, node):
        if node == self.head and node == self.tail:
            self.head = self.tail = None
        
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None
        
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None
        
        self.length -= 1

        return node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.addrMap = {}
        self.ll = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.addrMap:
            node = self.addrMap[key]
            self.ll.deleteNode(node)
            self.ll.addNode(node)
            return self.ll.getData(node)
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.addrMap:
            node = self.addrMap[key]
            self.ll.deleteNode(node)
            node.val = value
            self.ll.addNode(node)
        
        elif self.ll.length < self.capacity:
            node = self.ll.addData(value, key)
            self.addrMap[key] = node
        
        else:
            lestVal = self.ll.getHead()
            self.ll.deleteNode(lestVal)
            delKey = self.ll.getKey(lestVal)
            self.addrMap.pop(delKey)

            node = self.ll.addData(value, key)
            self.addrMap[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)