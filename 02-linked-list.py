class LinkedList:
    '''Doubly linked list class'''
    
    class Node:
        '''Node class to store data and pointers to next and previous nodes'''
        def __init__(self, data, p_prev, p_next):
            self.data = data
            self.next = p_next
            self.prev = p_prev

    def __init__(self):
        '''Initializes linked list object with a head and tail pointer'''
        self.head = None
        self.tail = None
        self.length = 0

    def _find(self, k):
        '''returns a node at position k'''
        if k >= self.length or k < 0:
            raise IndexError('index out of bounds')
        if 2 * k < self.length:
            node = self.head
            for i in range(k):
                node = node.next
        else:
            node = self.tail
            for i in range(self.length - k - 1):
                node = node.prev
        return node

    def append(self, x):
        '''adds element to the tail of the linked list'''
        if self.head is None:
            self.head = self.Node(x, None, None)
            self.tail = self.head
        else:
            self.tail.next = self.Node(x, self.tail, None)
            self.tail = self.tail.next
        self.length += 1

    def prepend(self, x):
        '''appends element to the head of the linked list'''
        if self.head is None:
            self.head = self.Node(x, None, None)
            self.tail = self.head
        else:
            self.head.prev = self.Node(x, None, self.head)
            self.head = self.head.prev
        self.length += 1

    def pop_tail(self):
        '''removes element from the tail of the linked list'''
        data = self.tail.data

        if self.tail is None:
            raise IndexError('pop from empty list') 
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.length -= 1
        return data

    def pop_head(self):
        '''removes element from the head of the linked list'''
        data = self.head.data

        if self.head is None:
            raise IndexError('pop from empty list')
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return data
        else:
            self.head = self.head.next
            self.head.prev = None
        
        self.length -= 1
        return data

    def add_to(self, x, k):
        '''adds element at a given position'''
        if k > self.length or k < 0:
            raise IndexError('index out of bounds')
        elif k == 0:
            self.prepend(x)
        elif k == self.length:
            self.append(x)
        else:
            node = self._find(k)
            node.prev = self.Node(x, node.prev, node)
            node.prev.prev.next = node.prev
        self.length += 1

    def remove_from(self, k):
        '''removes element at a given position'''
        if k >= self.length or k < 0:
            raise IndexError('index out of bounds')
        elif k == 0:
            self.pop_head()
        elif k == self.length - 1:
            self.pop_tail()
        else:
            node = self._find(k)
            node.prev.next = node.next
            node.next.prev = node.prev
            del node
        self.length -= 1


if __name__ == "__main__":

    ex = LinkedList()
    
    ex.append(8)
    ex.append(9)
    ex.append(20)
    
    ex.prepend(5)
    ex.prepend(2)
    
    ex.add_to(3, 3)
    ex.remove_from(2)

    node = ex.head 
    for i in range(ex.length):
        print(node.data)
        node = node.next


