class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        left_child, right_child = None, None
        if self.left is not None:
            left_child = self.left.val
        if self.right is not None:
            right_child = self.right.val
        return "Node " + str(self.val) + " - left child: " + str(left_child) + ", right child: " + str(right_child)


class BinaryTree:

    def __init__(self, root, size=1):
        self.root = root
        self.size = size

    def _get_elements_helper(self, current_node, nodes):
        nodes.append(current_node.val)
        if current_node.right is not None:
            self._get_elements_helper(current_node.right, nodes)
        if current_node.left is not None:
            self._get_elements_helper(current_node.left, nodes)
        return nodes

    def get_elements(self):
        nodes = []
        if self.root is not None:
            return self._get_elements_helper(self.root, nodes)
        else:
            return nodes

    def _insert_helper(self, current_node, new_node):
        if current_node.val < new_node.val:  # go to right child
            if current_node.right is None:
                current_node.right = new_node
                self.size += 1
            else:
                self._insert_helper(current_node.right, new_node)
        elif current_node.val > new_node.val:  # go to left child
            if current_node.left is None:
                current_node.left = new_node
                self.size += 1
            else:
                self._insert_helper(current_node.left, new_node)
        else:
            print("Insertion not possible - Node " + str(new_node.val) + " already in tree!")

    def insert(self, new_node):
        if self.root is not None:
            self._insert_helper(self.root, new_node)
        else:
            self.root = new_node

    def _get_node_helper(self, current_node, val):
        if current_node.val < val:
            if current_node.right is not None:
                return self._get_node_helper(current_node.right, val)
            else:
                print("No node with value " + str(val) + " in this tree!")
        elif current_node.val > val:
            if current_node.left is not None:
                return self._get_node_helper(current_node.left, val)
            else:
                print("No node with value " + str(val) + " in this tree!")
        else:
            return current_node

    def get_node(self, val):
        if self.root is not None:
            return self._get_node_helper(self.root, val)
        else:
            return None


if __name__ == '__main__':
    my_tree = BinaryTree(Node("Jens"))
    my_tree.insert(Node("Anja"))
    my_tree.insert(Node("Mario"))
    my_tree.insert(Node("Julia"))
    my_tree.insert(Node("Olaf"))
    my_tree.insert(Node("Erik"))
    my_tree.insert(Node("Alina"))
    my_tree.insert(Node("Olaf"))
    print(my_tree.get_node("Mario"))
    print(my_tree.get_node("Alina"))
    print(my_tree.get_node("Jens"))
    print(my_tree.get_elements())
    print(my_tree.size)
