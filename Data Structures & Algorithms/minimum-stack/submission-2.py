class MinStack:

    def __init__(self):

        self.min_stack = list()
        self.stack = list()
        
    def push(self, val: int) -> None:

        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)
        
    def pop(self) -> None:

        ele = self.stack.pop()
        if len(self.min_stack) !=0 and ele == self.min_stack[-1]:
            self.min_stack.pop()
        
    def top(self) -> int:
        
        return self.stack[-1]
        

    def getMin(self) -> int:

        return self.min_stack[-1]

        
        
