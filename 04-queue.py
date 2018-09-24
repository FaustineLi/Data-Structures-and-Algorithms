import importlib
m = importlib.import_module('02-linked-list')
LinkedList = m.LinkedList

class Queue:
    '''First in, first out stack data structure class'''

    def __init__(self):
        self.queue = LinkedList()

    def __repr__(self):
        '''Provides a string representation of the linked list'''
        s = '<'
        node = self.queue.head
        while node is not None:
            s += str(node.data)
            if node is not self.queue.tail: 
                s += ', '
            node = node.next
        s += '>'
        return s

    def __len__(self):
        '''Returns number of nodes in the linked list'''
        return self.queue.length

    def __getitem__(self, k):
        '''Special method for accessing a node'''
        node = self.queue._find(k)
        return node.data

    def __setitem__(self, k, x):
        '''Special method for acessing a node to modify it'''
        node = self.queue._find(k)
        node.data = x

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        return self.queue.pop_head()


if __name__ == "__main__":
    ex = Queue()

    ex.push(3)
    ex.push(2)
    ex.push(1)
    print(ex)

    ex[1] = 17
    print(ex)

    for i in range(len(ex)):
        print(ex.pop())