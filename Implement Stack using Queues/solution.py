class Queue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def enqueue(self, x):
        node = Queue.Node(x)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1
    def dequeue(self):
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.count -= 1
        return data
    def peek(self):
        return self.head.data if self.head else None
    def empty(self):
        return self.head is None
    def size(self):
        return self.count
    def stack_push(self, q1, q2, x):
        q2.enqueue(x)
        while not q1.empty():
            q2.enqueue(q1.dequeue())
        q1.head, q1.tail, q1.count = q2.head, q2.tail, q2.count
        q2.head = q2.tail = None
        q2.count = 0
    def stack_pop(self, q1):
        return q1.dequeue()
    def stack_top(self, q1):
        return q1.peek()
    def stack_empty(self, q1):
        return q1.empty()

class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.ops = Queue()
    def push(self, x: int) -> None:
        self.ops.stack_push(self.q1, self.q2, x)
    def pop(self) -> int:
        return self.ops.stack_pop(self.q1)
    def top(self) -> int:
        return self.ops.stack_top(self.q1)
    def empty(self) -> bool:
        return self.ops.stack_empty(self.q1)
        
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
