class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class Tree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def traversal(self, node):
        result = []
        def inorder_traversal(_node):
            if _node is None:
                return
            inorder_traversal(_node.left)
            result.append(_node.data)
            inorder_traversal(_node.right)
        inorder_traversal(node)
        if node == self.root:
            print(' '.join(map(str, result)))
        return result
    def insert(self, node, data):
        if node is None:
            return Node(data)
        if data <= node.data:
            node.left=self.insert(node.left, data)
            node.left.parent = node
        else:
            node.right=self.insert(node.right, data)
            node.right.parent = node
        return node
    def search(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        if data < node.data:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)
    @staticmethod
    def min_value_node(node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    @staticmethod
    def max_value_node(node):
        current = node
        while current.right is not None:
            current = current.right
        return current
    def delete(self, node, data):
        if node is None:
            return None
        if data < node.data:
            node.left = self.delete(node.left, data)
            if node.left:
                node.left.parent = node
        elif data > node.data:
            node.right = self.delete(node.right, data)
            if node.right:
                node.right.parent = node
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self.min_value_node(node.right)
                node.data = temp.data
                node.right = self.delete(node.right, temp.data)
        return node