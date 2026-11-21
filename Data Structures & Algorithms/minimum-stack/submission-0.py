class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        self.minStack = []
    

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (val <= self.min):
            self.minStack.append(self.min)
            self.min = val

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
            
        if self.stack[-1] == self.min:
            if len(self.minStack) > 0:
                self.min = self.minStack.pop()
            else:
                self.min = float('inf')
            
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        if len(self.stack) <= 0:
            return None
            
        return self.min
