class BstMap:
    '''Map implemented using binary search trees'''
    
    class Node:
        def __init__(self, key, value):
            self.key  = key
            self.value = value
            self.left  = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert_helper(self, key, value, node):
        if node is None:
            return Node(key, value)
        elif key > node.key:
           node.right = self.insert_helper(key, value, node.right)
        elif key < node.key:
            node.left = self.insert_helper(key, value, node.left)
        else:
            node.value = value
        return node

    def insert(self, key, value):
        root = self.insert_helper(key, value, self.root)

    def printInorder(self, node = self.root):
        if node is not None:
            self.printInorder(node.left)
            print(node.value)
            self.printInorder(node.right)

    def remove(self, x):
        pass

    def find(self, x):
        pass

#------------------------------------------

ex = BstMap()
ex.insert("apple", 5)
