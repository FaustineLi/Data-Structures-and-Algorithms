import importlib
m = importlib.import_module('02-linked-list')
LinkedList = m.LinkedList

class Stack:
    '''First in, last out stack data structure class'''

    def __init__(self):
        self.stack = LinkedList()

    def __repr__(self):
        '''Provides a string representation of the linked list'''
        s = '<'
        node = self.stack.head
        while node is not None:
            s += str(node.data)
            if node is not self.stack.tail: 
                s += ', '
            node = node.next
        s += '>'
        return s

    def __len__(self):
        '''Returns number of nodes in the linked list'''
        return self.stack.length

    def __getitem__(self, k):
        '''Special method for accessing a node'''
        node = self.stack._find(k)
        return node.data

    def __setitem__(self, k, x):
        '''Special method for acessing a node to modify it'''
        node = self.stack._find(k)
        node.data = x

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop_tail()


if __name__ == "__main__":
    ex = Stack()

    ex.push(3)
    ex.push(2)
    ex.push(1)
    print(ex)

    ex[1] = 17
    print(ex)

    for i in range(len(ex)):
        print(ex.pop())