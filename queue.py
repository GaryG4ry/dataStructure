class Queue:
    def __init__(self):
        self.queue = list()

    def add(self, dataval):
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
        else:
            return

    def size(self):
        return len(self.queue)

    def remove(self):
        if self.size() >= 0:
            self.queue.pop()
        else:
            return
        