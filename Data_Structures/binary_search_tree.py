class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if self.data < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            if self.data == data:
                return "This node already in tree"

    def in_order_traversal(self):
        nodes = []

        if self.left:
            nodes += self.left.in_order_traversal()

        nodes.append(self.data)

        if self.right:
            nodes += self.right.in_order_traversal()

        return nodes

    def pre_order_traversal(self):
        nodes = []

        nodes.append(self.data)

        if self.left:
            nodes += self.left.in_order_traversal()

        if self.right:
            nodes += self.right.in_order_traversal()

        return nodes

    def post_order_traversal(self):
        nodes = []

        if self.left:
            nodes += self.left.in_order_traversal()

        if self.right:
            nodes += self.right.in_order_traversal()

        nodes.append(self.data)

        return nodes

    def find_value(self, value):
        if self.data == value:
            return True

        if self.data > value:
            if self.left:
                return self.left.find_value(value)
            else:
                return False

        if self.data < value:
            if self.right:
                return self.right.find_value(value)
            else:
                return False

    def max_node(self):
        if self.right is None:
            return self.data
        return self.right.max_node()

    def min_node(self):
        if self.left is None:
            return self.data
        return self.left.min_node()

    def sum_of_nodes(self):
        left_sum = self.left.sum_of_nodes() if self.left else 0
        right_sum = self.right.sum_of_nodes() if self.right else 0

        return self.data + left_sum + right_sum


def create_bst(nodes):
    root = Node(nodes[0])

    for i in range(1, len(nodes)):
        root.insert(nodes[i])

    return root


if __name__ == '__main__':
    nodes = [8, 3, 10, 1, 6, 14, 4, 7, 13]

    tree = create_bst(nodes)

    print(tree.max_node())
    print(tree.min_node())

    print(tree.find_value(1))
    print(tree.find_value(99))

    print(tree.sum_of_nodes())

    print(tree.in_order_traversal())
