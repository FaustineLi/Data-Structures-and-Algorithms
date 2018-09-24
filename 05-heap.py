class Heap:
    '''Class for the binary heap data structure'''
    
    def __init__(self, A=None, mode='max'):
        '''
        Initializes a max heap using an array of elements. The heap is 
        rooted at the first element. The left child of node n is at 
        location 2n + 1 and the right child is at location 2n + 2. 
        '''
        self.heap = []
        self.mode = mode
        if A is not None:
            self.heap = A
            self.heap = self._heapify()

    def __len__(self):
        '''returns length of heap'''
        return len(self.heap)

    def __repr__(self):
        '''prints heap elements'''
        return repr(self.heap)

    def _cmp(self, x, y):
        '''comparison function for the min / max heap'''
        if self.mode == 'max':
            return x < y
        if self.mode == 'min':
            return x > y

    def _sift_down(self, k, n = None):
        '''
        Moves a heap
        '''
        A = self.heap
        i = 2 * k + 1
        
        if not n:
            n = len(A) - 1

        while i < n:
            if i + 1 < n and self._cmp(A[i], A[i + 1]):
                i += 1

            if self._cmp(A[k], A[i]):
                A[i], A[k] = A[k], A[i]
                k = i
                i *= 2
            else:
                break
    
    def _sift_up(self, k):
        '''

        '''
        A = self.heap
        i = (k - 1) // 2
        while i >= 0 and self._cmp(A[i], A[k]):
            A[i], A[k] = A[k], A[i]
            k = i
            i = (i - 1) // 2

    def _heapify(self):
        '''
        Constructs a max or min heap from a list of elements. We do this by
        starting with the second to last level and performing the sift down
        operation to build progressively larger heaps. 
        '''
        i = (len(self.heap) - 1) // 2
        while i >= 0:
            self._sift_down(i)
            i -= 1
        return self.heap

    def insert(self, x):
        '''
        Inserts an element to the heap. We insert the element as the right
        most child and fix the max / min heap property by repeatedly using
        the shift up operation.
        '''
        n = len(self.heap) - 1
        self.heap.append(x)
        self._sift_up(n)

    def pop(self):
        '''
        Returns and removes the root of the heap. We swap the right most child
        with the root of the heap, remove the root, and fix the max / min 
        heap property by repeatedly calling the shift down operation. 
        '''
        n = len(self.heap) - 1
        self.heap[0], self.heap[n] = self.heap[n], self.heap[0]
        root = self.heap.pop(n)
        self._sift_down(0)
        return root

    def sort(self):
        '''
        Returns the elements in sorted order (max heap) or reverse sorted order
        (min heap). We do this by swapping the root of the heap with the next
        unsorted element and performing the sift down operation on the new element.
        '''
        i = len(self.heap) - 1
        while i > 0:
            print(self.heap)
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self._sift_down(0, i)
            i -= 1


if __name__ == '__main__':

    A = [1, 8, 2, 6, 7, 5, 3]
    ex = Heap(A, mode='max')
    #print(ex)

    ex.insert(11)
    ex.insert(9)
    ex.insert(4)
    #print(ex)

    ex.pop()
    #print(ex)

    ex.sort()
    #print(ex)
    