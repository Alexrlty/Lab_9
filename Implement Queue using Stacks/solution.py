import queue

class MyQueue:
    def __init__(self):
        self.in_stack = queue.LifoQueue() # for real stack
        self.out_stack = queue.LifoQueue() # to get first element

    def push(self, x: int) -> None:
        self.in_stack.put(x)

    def _move(self) -> None: # move obj from in_stack into out_stack in invertet order
        if self.out_stack.empty():
            while not self.in_stack.empty():
                self.out_stack.put(self.in_stack.get())

    def pop(self) -> int:
        self._move()
        return self.out_stack.get()

    def peek(self) -> int:
        self._move()
        x = self.out_stack.get()
        self.out_stack.put(x)
        return x

    def empty(self) -> bool:
        return self.in_stack.empty() and self.out_stack.empty()

