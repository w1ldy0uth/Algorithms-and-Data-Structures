class Node:
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.pointer = pointer


class Linked_list:
    def __init__(self):
        self.head = None

    def front_add(self, data):
        self.head = Node(data=data, pointer=self.head)

    def end_add(self, data):
        if not self.head:
            self.head = Node(data=data)
            return 0
        curr = self.head
        while curr.pointer:
            curr = curr.pointer
        curr.pointer = Node(data=data)

    def isempty(self):
        return self.head is None

    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.pointer
        if prev is None:
            self.head = curr.pointer
        elif curr:
            prev.pointer = curr.pointer
            curr.pointer = None

    def get_last(self):
        temp = self.head
        while temp.pointer is not None:
            temp = temp.pointer
        return temp.data

    def print_ll(self):
        node = self.head
        while node is not None:
            if node.pointer is not None:
                print(node.data, end=" -> ")
            else:
                print(node.data)
            node = node.pointer


if __name__ == '__main__':
    l_list = Linked_list()
    l_list.front_add(0)
    for i in range(1, 10):
        l_list.end_add(i)

    l_list.print_ll()

    print(l_list.get_last())
