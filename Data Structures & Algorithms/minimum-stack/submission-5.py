class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        self.minStack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min>val:
            self.min = val
        self.minStack.append(self.min)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        self.min = self.minStack[-1] if self.minStack else float('inf')
    def top(self) -> int:
        top = self.stack[-1]
        return top

    def getMin(self) -> int:
        return self.minStack[-1]
            
        
