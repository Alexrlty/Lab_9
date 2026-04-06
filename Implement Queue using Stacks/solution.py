class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        node = Node(x)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def pop(self) -> int:
        data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return data

    def peek(self) -> int:
        return self.head.data

    def empty(self) -> bool:
        return self.head is None
