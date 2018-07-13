class MaxHeap:
    '''Class for a max heap data structure'''

    def __init__(self, A = None):
        '''
        Initializes a max heap using an array of elements. Because 
        Python is zero indexed we modify the heap math.
        '''
        if A:
            self.heap = self.max_heapify(A)
        else:
            self.heap = []

    def __len__(self):
        '''returns length of heap'''
        return len(self.heap)

    def __str__(self):
        '''prints heap elements'''
        return str(A.heap)

    def _sink(self, A, k, n = None):
        '''
        Moves an node down until both children are smaller than it. 
        We swap the parent with its largest child. We sink up to 
        a position n (useful for heap sort).
        '''
        i = 2 * k + 1
        
        if not n:
            n = len(A)

        while i < n:
            if i + 1 < n and A[i + 1] > A[i]:
                i += 1

            if A[k] < A[i]:
                A[i], A[k] = A[k], A[i]
                k = i
                i *= 2
            else:
                break
    
    def _swim(self, A, k):
        '''
        Moves an node up by swapping the child with its parent 
        until its parent is bigger than it.
        '''
        i = (k - 1) // 2
        while i >= 0 and A[k] > A[i]:
            A[i], A[k] = A[k], A[i]
            k = i
            i = (i - 1) // 2

    def insert(self, k):
        '''
        Inserts an element into the heap by adding it to the end and 
        restoring the max heap property with the swim operation. 
        '''
        self.heap.append(k)
        self._swim(self.heap, len(self.heap) - 1)

    def pop_max(self):
        '''
        Removes and returns the max element. We do this by swapping 
        the first and last elements, removing the last element, and 
        retoring the max heap property with the sink operation. 
        '''
        n = len(self.heap) - 1
        self.heap[0], self.heap[n] = self.heap[n], self.heap[0]
        mx = self.heap.pop(n)
        self._sink(self.heap, 0)
        return mx

    def max_heapify(self, A):
        '''
        Constructs a max heap from a list of elements. We do this by
        starting with the second to last level and performing the sink
        operation to build progressively larger max heaps. 
        '''
        i = (len(A) - 1) // 2
        while i >= 0:
            self._sink(A, i)
            i -= 1
        return A

    def sort(self):
        '''
        Sorts the heap using heap sort. We swap the maximum element to the
        back of the array and remove it from the heap. We then fix the max 
        heap property with sink operations. 
        '''
        i = len(self.heap) - 1
        while i > 0:
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self._sink(self.heap, 0, i)
            i -= 1 

       
if __name__ == '__main__':

    A = [1, 4, 2, 7, 6, 5, 3]

    A = MaxHeap(A)
    print(A)

    A.insert(9)
    A.insert(11)
    A.insert(5)
    print(A)

    A.pop_max()
    print(A)

    A.sort()
    print(A)
    