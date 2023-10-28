class Node:
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        node = self.end
        self.end = self.end.pref
        node.pref = None
        return node.data

    def push(self, val):
        if self.end == None:
            self.end = Node(val)
        else:
            newNode = Node(val)
            newNode.pref = self.end
            self.end = newNode

    def print(self):
        n = self.end
        while n is not None:
            print(n.data)
            n = n.pref
