class LinkedList:
    '''Doubly linked list class'''
    
    class Node:
        def __init__(self, data, p_prev, p_next):
            self.data = data
            self.next = p_next
            self.prev = p_prev

    def __init__(self, A = None):
        self.head = None
        self.tail = None
        self.length = 0
        if A is not None:
            for x in A:
                self.append(x)

    def __len__(self):
        return self.length

    def __str__(self):
        node = self.head
        string_rep = '['
        
        while node is not None:
            string_rep += str(node.data)
            node = node.next
            if node is not None:
                string_rep += ', '
        
        string_rep += ']'
        return(string_rep)

    def __getitem__(self, ind):
        if ind < 0 or ind >= self.length:
            raise IndexError("index out of bounds")

        if 2 * ind < self.length:
            node = self.head
            for i in range(ind):
                node = node.next 
        else:
            node = self.tail
            for i in range(self.length - ind - 1):
                node = node.prev
        return node.data
        
    def __setitem__(self, ind, x):
        if ind < 0 or ind >= self.length:
            raise IndexError("index out of bounds")

        if 2 * ind < self.length:
            node = self.head
            for i in range(ind):
                node = node.next 
        else:
            node = self.tail
            for i in range(self.length - ind - 1):
                node = node.prev
        node.data = x

    def append(self, x):
        '''adds element to the tail of the linked list'''
        if self.head is None:
            self.head = LinkedList.Node(x, None, None)
            self.tail = self.head
        else:
            self.tail.next = LinkedList.Node(x, self.tail, None)
            self.tail = self.tail.next
        self.length += 1

    def prepend(self, x):
        '''appends element to the head of the linked list'''
        if self.head is None:
            self.head = LinkedList.Node(x, None, None)
            self.tail = self.head
        else:
            self.head.prev = LinkedList.Node(x, None, self.head)
            self.head = self.head.prev
        self.length += 1

    def remove_tail(self):
        '''removes element from the tail of the linked list'''
        if self.head is None:
            raise IndexError('remove from empty linked list')
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1

    def remove_head(self):
        '''removes element from the head of the linked list'''
        if self.head is None:
            raise IndexError('remove from empty linked list')
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1

    def add_to(self, pos, x):
        '''adds element to a given position'''
        if pos > self.length or pos < 0:
            raise IndexError('index out of bounds')
        elif pos == 0:
            self.prepend(x)
        elif pos == self.length:
            self.append(x)
        else:
            node = self.head
            for i in range(pos):
                node = node.next
            node.prev = LinkedList.Node(x, node.prev, node)
            node.prev.prev.next = node.prev
            self.length += 1

    def remove_from(self, pos):
        '''removes element at a given position'''
        if pos >= self.length or pos < 0:
            raise IndexError('index out of bounds')
        elif pos == 0:
            self.remove_head()
        elif pos == self.length - 1:
            self.remove_tail()
        else:
            node = self.head
            for i in range(pos):
                node = node.next
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
            del node

#----------------------------------------------------

ex = LinkedList([3, 4, 1])
ex.append(8)
ex.append(9)
ex.append(20)
print(ex)
ex.add_to(3, 0)
print(ex)
ex.remove_from(2)
print(ex)
ex[5] = 11
print(ex)
