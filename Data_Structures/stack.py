class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.insert(0, item)

    def pop(self):
        del self.stack[0]

    def is_empty(self):
        return len(self.stack) == 0

    def print_stack(self):
        for i in self.stack:
            if i != self.stack[len(self.stack)-1]:
                print(i, end=", ")
            else:
                print(i)


if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)
    stack.print_stack()

    stack.pop()
    stack.print_stack()
