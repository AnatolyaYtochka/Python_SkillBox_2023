class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:

    def __init__(self):
        self.head = None

    def get(self, index):
        count = 0
        node = self.head
        while count != index:
            node = node.next
            count += 1
        return node.data

    def push(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            return
        node = self.head
        while(node.next):
            node = node.next
        node.next = newNode
            
    def remove(self, index):
        node = self.head
        if node and index == 0: 
            self.head = node.next
            node = None
        count = 0
        previousNode = None
        while node and count != index:
            previousNode = node
            node = node.next
            count += 1
        if not previousNode: return
        previousNode.next = node.next
        node = None
    
    def insert(self, n, val):
        newNode = Node(val)
        node = self.head
        pos = 0
        while(node and pos + 1 != n):
            pos += 1
            node = node.next
        if node:
            newNode.next = node.next
            node.next = newNode

    def print(self):
        n = self.head
        while n:
            print(n.data)
            n = n.next
            
            