class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        res = self.stack[-1]
        return res

    def getMin(self) -> int:
        temp = []
        minI = self.stack[-1]

        while len(self.stack):
            minI = min(minI, self.stack[-1])
            temp.append(self.stack.pop())

        while len(temp):
            self.stack.append(temp.pop())
        
        return minI
