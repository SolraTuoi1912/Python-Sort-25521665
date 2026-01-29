import numpy as np
import time

a = np.loadtxt("test03.inp", dtype = float)

def heapify(n, i):
    global a
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if (left < n and a[left] > a[largest]):
        largest = left
    if (right < n and a[right] > a[largest]):
        largest = right
    if (largest != i):
        a[i], a[largest] = a[largest], a[i]
        heapify(n, largest)

def build():
    global a
    n = a.size
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

def HeapSort():
    global a
    n = a.size
    build()
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(i, 0)

start_time = time.perf_counter()

HeapSort();

end_time = time.perf_counter()

print(a)
print("Time:", end_time - start_time, "s")
