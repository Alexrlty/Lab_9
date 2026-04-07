class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    def __init__(self):
        self.top_node = None
        self.count = 0
    def push(self, x):
        node = Stack.Node(x)
        node.next = self.top_node
        self.top_node = node
        self.count += 1
    def pop(self):
        if not self.top_node:
            return None
        data = self.top_node.data
        self.top_node = self.top_node.next
        self.count -= 1
        return data
    def peek(self):
        return self.top_node.data if self.top_node else None
    def empty(self):
        return self.top_node is None
    def size(self):
        return self.count
    def queue_push(self, in_stack, out_stack, x):
        in_stack.push(x)
    def queue_pop(self, in_stack, out_stack):
        if out_stack.empty():
            while not in_stack.empty():
                out_stack.push(in_stack.pop())
        return out_stack.pop()
    def queue_peek(self, in_stack, out_stack):
        if out_stack.empty():
            while not in_stack.empty():
                out_stack.push(in_stack.pop())
        return out_stack.peek()
    def queue_empty(self, in_stack, out_stack):
        return in_stack.empty() and out_stack.empty()

class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.ops = Stack()
    def push(self, x: int) -> None:
        self.ops.queue_push(self.s1, self.s2, x)
    def pop(self) -> int:
        return self.ops.queue_pop(self.s1, self.s2)
    def peek(self) -> int:
        return self.ops.queue_peek(self.s1, self.s2)
    def empty(self) -> bool:
        return self.ops.queue_empty(self.s1, self.s2)
