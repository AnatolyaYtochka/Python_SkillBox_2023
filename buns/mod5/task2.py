#task2
class Node:
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        val = self.items[0]
        self.items = self.item[1:]
        return val

    def push(self, val):
        if self.end is None:
            self.start = Node(val)
            self.end = self.start
        else:
            self.end.nref = Node(val)
            self.end.nref.pref = self.end
            self.end = self.end.nref

    def insert(self, n, val):
        if self.start is None:
            return
        x = self.start
        while x is not None:
            if x.data == n:
                break
            x = x.nref
        if x is not None:
            node = Node(val)
            node.pref = x
            node.nref = x.nref
            if x.nref is not None:
                x.nref.pref = node
            x.nref = node

    def print(self):
        n = self.start
        while n is not None:
            print(n.data)
            n = n.nref
            