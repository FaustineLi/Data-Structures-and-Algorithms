def bubble_sort(A):
    '''
    At each pass of the list, we swap adjacent pairs of values if
    the value at the current position is larger. At each pass of
    outer loop we only need to look at the unsorted portions. 
    '''
    for i in range(len(A)):
        for j in range(len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


def selection_sort(A):
    '''
    For each iteration, we incrementally sort the list by linearly searching 
    for the smallest value in the unsorted portion and bringing it to the
    front by swapping.
    '''
    for i in range(len(A)):
        min_i = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_i]:
                min_i = j
        A[i], A[min_i] = A[min_i], A[i]


def insertion_sort(A):
    '''
    At each pass of the top loop, we incrementatly sort the list by
    taking the next unsorted element (the key) and swapping elements
    until it is in the correct location. 
    '''
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1], A[j] = A[j], A[j + 1]
            j -= 1
   

def shell_sort(A):
    '''
    At each pass, we h-sort the sequence, interweaving h number of 
    sorted subsequences with items h apart. Insertion sort is used 
    to put elements in place. We use the 3h + 1 progression popularized 
    by Knuth and decrease h until the list is 1-sorted. 
    '''
    h = 1
    while (3 * h + 1) < len(A):
        h = 3 * h + 1
    
    while h >= 1:
        for start in range(h):
            for i in range(start + h, len(A), h):
                key = A[i]
                j = i - h
                while j >= 0 and A[j] > key:
                    A[j + h], A[j] = A[j], A[j + h]
                    j -= h
        h = (h - 1) // 3


def cycle_sort(A):
    '''
    A sorting algorithm that minimizes the number of write operations. The 
    element is only written to the array in its final location which 
    is found by counting the number of elements less than or equal to it. 
    This write displaces another element which becomes the next item to be placed. 
    A cycle of writing and displacing continues until a value is written to the 
    index at the start of the cycle. The sort is completed when every value in 
    the list is in the correct location. 

    One optimization is keeping a set of indexes that have been written to and
    skipping the cycle counting if it has already been seen.
    '''
    n = set()
    for start in range(len(A) - 1):
        if start not in n:
            n.add(start)
        else:
            continue 

        key = A[start]
        k = start
        for j in range(start + 1, len(A)):
            if A[j] <= key:
                k += 1

        if k == start:
            continue
        else:
            key, A[k] = A[k], key

        while k != start:
            k = start
            for j in range(start + 1, len(A)):
                if A[j] <= key:
                    k += 1

            n.add(key)       
            key, A[k] = A[k], key


def merge_sort(A):
    '''
    Recursively sorts the list by splitting the list in half
    until we reach the base case of a list of length one which 
    is trivially sorted. Then we merge the two halves together
    by comparing the elements of the two lists.
    '''
    if len(A) > 1:
        k = len(A) // 2
        L = A[:k]
        R = A[k:]
          
        merge_sort(L)
        merge_sort(R)

        right = left = 0
        for i in range(len(A)):
            if left == len(L):
                A[i:] = R[right:]
                break
            if right == len(R):
                A[i:] = L[left:]
                break

            if R[right] < L[left]:
                A[i] = R[right]
                right += 1
            else:
                A[i] = L[left]
                left += 1


def quick_sort(A, lo=0, hi=None):
    '''
    Recursively sorts a list by partitioning the array, creating 
    portions that are smaller and larger than a pivot value. 

    First, we pick a pivot value (here we pick the first element).
    We increment indexes until we find elements that are out of place 
    and swap them to their correct partitions. The array is correctly
    partitioned when the indexes cross. Finally we swap the pivot 
    to the correct location and continue with the recursion, 
    sorting the left and right sides. 

    If the list is already sorted, quick sort produces quadratic runtime. 
    To ensure performance, the array is randomly shuffled before sorting.
    '''
    if lo == 0 and hi is None:
        import random
        random.shuffle(A)
        hi = len(A) - 1

    if lo < hi:
        pivot = A[lo]
        i = lo + 1
        j = hi

        while i <= j:
            while i <= j and A[j] > pivot:
                j -= 1
            while i <= j and A[i] < pivot:
                i += 1
            
            if i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            
        A[j], A[lo] = A[lo], A[j]

        quick_sort(A, lo, j - 1)
        quick_sort(A, j + 1, hi)


def heap_sort(A):
    '''
    Sorts array by constructing a max binary heap and incrementally
    moving the largest element to the back. 

    We represent the heap on the array so that each parent node at k 
    has children at positions 2k + 1 and 2k + 2. The max heap property 
    is that each parent node is larger than its two child nodes with the 
    maximum node at the top of the tree.

    We incrementally constuct the heap from the bottom up. Starting with 
    the second to last level (the last level nodes are trivially heaps), 
    we build the heap by applying the sift down operation on each node.

    We sort the array by incrementally removing the largest element from the
    heap. We do this by swaping the first and last array elements, shrinking
    the size of the heap, and fixing the max heap property by applying the 
    sift down operation. In this way, we grow a portion of the array that 
    is sorted.
    '''

    def sift_down(A, k, n):
        '''
        Moves an node down until both children are smaller than it. 
        We swap the parent with its largest child. We go down to a 
        position n (important for the sorting part). 
        '''
        i = 2 * k + 1

        while i < n:
            if i + 1 < n and A[i + 1] > A[i]:
                i += 1

            if A[k] < A[i]:
                A[i], A[k] = A[k], A[i]
                k = i
                i = 2 * i + 1
            else:
                break

    i = (len(A) - 1) // 2
    while i >= 0:
        sift_down(A, i, len(A))
        i -= 1

    i = len(A) - 1
    while i > 0:
        A[0], A[i] = A[i], A[0]
        sift_down(A, 0, i)
        i -= 1


def radix_sort(A, n=None):
    '''
    A non-comparitive sort that sorts integer keys by digits.
    We sort by the least significant digit to the most significant
    digit in base n using counting sort or any other stable sort. 
    
    For each digit, we create an auxilliary array and add elements 
    by indexing into the digit "pigeonhole". We read out the 
    results by traversing the auxilliary array.  
    '''
    if n is None:
        n = len(A)

    d = 0
    while n ** d <= max(A):
        L = [[] for i in range(n)]
        for i in range(n):
            k = (A[i] // (n ** d)) % n
            L[k].append(A[i]) 

        h = 0
        for i in range(n):
            for j in range(len(L[i])):
                A[h] = L[i][j]
                h += 1    
        d += 1

        
if __name__ == '__main__':

    import time
    import random

    A = list(range(10000))
    sorting_functions = [
        bubble_sort,
        cycle_sort, 
        insertion_sort, 
        selection_sort,
        shell_sort, 
        heap_sort, 
        merge_sort, 
        quick_sort, 
        radix_sort
    ]

    for sort in sorting_functions:
        random.seed(0)
        random.shuffle(A)
        
        start = time.time()
        sort(A)
        end = time.time()
        
        if A == sorted(A):
            print(sort.__name__, end - start)
