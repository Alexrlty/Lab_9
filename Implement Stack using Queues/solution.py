import queue

class MyStack:

    def __init__(self):
        self.in_stack = queue.LifoQueue() # for real stack

    def push(self, x: int) -> None:
        self.in_stack.put(x)

    def pop(self) -> int:
        return self.in_stack.get()

    def top(self) -> int:
        x = self.in_stack.get()
        self.in_stack.put(x)
        return x
        
    def empty(self) -> bool:
        return self.in_stack.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
