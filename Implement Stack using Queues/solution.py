import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        node = Node(x)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def pop(self) -> int:
        head_2 = self.head
        if not head_2:
            return
        if not head_2.next:
            data = head_2.data
            head_2.next = None
            self.head = None
            self.tail = None
            return data

        while True:
            if not head_2.next.next:
                data = head_2.next.data
                head_2.next = None
                self.tail = head_2
                break
            head_2 = head_2.next
        return data

    def top(self) -> int:
        return self.tail.data
        
    def empty(self) -> bool:
        return not self.head
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
