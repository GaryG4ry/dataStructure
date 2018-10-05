class Stack(object):
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    def peek(self):
        return self.stack[0]

    def remove(self):
        if len(self.stack) <= 0:
            return
        else:
            return self.stack.pop()


s = Stack()
s.add(123)
s.add(456)
s.add(789)
print(s.peek())
print(s.remove())
print(s.remove())