class MyQueue:

    def __init__(self):
        self.stack1 = [] # for push
        self.stack2 = [] # for pop
        
    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1: self.stack2.append(self.stack1.pop())
        return self.stack2.pop()   

    def peek(self) -> int:
        if self.stack2: return self.stack2[-1]
        else: return self.stack1[0]

    def empty(self) -> bool:
        return self.stack1 == [] and self.stack2 == []
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())
