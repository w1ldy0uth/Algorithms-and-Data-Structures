class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        self.queue.pop()

    def is_empty(self):
        return self.queue == []

    def print_queue(self):
        for item in self.queue:
            if item != self.queue[len(self.queue) - 1]:
                print(item, end=', ')
            else:
                print(item)


if __name__ == '__main__':
    qu = Queue()
    qu.is_empty()
    for i in range(10):
        qu.enqueue(i)
    qu.print_queue()
    qu.dequeue()
    qu.print_queue()
