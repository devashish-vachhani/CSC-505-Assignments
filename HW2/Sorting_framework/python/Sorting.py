import math

class Sorting:
    def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0
        
    def merge(self, p, q, r):
        A = self.sorting_array
        nL = q - p + 1
        nR = r - q
        
        L = [0] * nL
        R = [0] * nR
        
        for i in range(0, nL):
            L[i] = A[p+i]
        for j in range(0, nR):
            R[j] = A[q+j+1]
        i = 0
        j = 0
        k = p
        while i < nL and j < nR:
            self.comparison_count += 1
            if L[i] <= R[j]:
                A[k] = L[i]
                i = i + 1
            else:
                A[k] = R[j]
                j = j + 1
            k = k + 1
        while i < nL:
            A[k] = L[i]
            i = i + 1
            k = k + 1
        while j < nR:
            A[k] = R[j]
            j = j + 1
            k = k + 1

    def merge_sort(self, p, r):
        A = self.sorting_array
        if p >= r:
            return
        q = int(math.floor((p+r)/2))
        self.merge_sort(p, q)
        self.merge_sort(q+1, r)
        self.merge(p, q, r)
        
    def max_heapify(self, i, n):
        A = self.sorting_array
        l = 2*i + 1
        r = 2*i + 2
        largest = i
        if l <= n-1: 
            self.comparison_count += 1
            if A[l] > A[i]:
                largest = l
        if r <= n-1: 
            self.comparison_count += 1
            if A[r] > A[largest]:
                largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.max_heapify(largest, n)
        
    def build_max_heap(self):
        A = self.sorting_array
        n = len(A)
        for i in range(int(math.floor((n-1)/2)), -1, -1):
            self.max_heapify(i, n)

    def heap_sort(self):
        A = self.sorting_array
        n = len(A)
        self.build_max_heap()
        for i in range(n-1, 0, -1):
            A[0], A[i] = A[i], A[0]
            n = n - 1
            self.max_heapify(0, n)

    def insertion_sort(self):
        A = self.sorting_array
        n = len(A)
        for i in range(1, n):
            key = A[i]
            j = i-1
            while j >= 0 and A[j] > key:
                self.comparison_count += 1
                A[j+1] = A[j]
                j = j-1
            if(j >= 0): 
                self.comparison_count += 1
            A[j+1] = key