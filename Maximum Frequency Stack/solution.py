import queue

class FreqStack:
    def __init__(self):
        self.stack = {}
        self.stack_freq = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        obj = self.stack.get(val, 0) + 1
        self.stack[val] = obj
        if obj > self.max_freq:
            self.max_freq = obj
        if obj not in self.stack_freq:
            self.stack_freq[obj] = queue.LifoQueue()
        self.stack_freq[obj].put(val)

    def pop(self) -> int:
        value = self.stack_freq[self.max_freq].get()
        self.stack[value] -= 1
        if self.stack_freq[self.max_freq].empty():
            self.max_freq -= 1
        return value

