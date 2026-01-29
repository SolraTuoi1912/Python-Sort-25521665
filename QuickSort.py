import numpy as np
import time

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
            
        j -= 1
        while arr[j] > pivot:
            j -= 1
            
        if i >= j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort_inplace(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort_inplace(arr, low, p)
        quick_sort_inplace(arr, p + 1, high)

try:
    a = np.loadtxt('test01.inp', dtype=float)
    
    start_time = time.perf_counter()
    quick_sort_inplace(a, 0, len(a) - 1)
    end_time = time.perf_counter()
    
    print(f"Sắp xếp xong 10^6 số trong: {end_time - start_time:.4f}s")
    
    np.savetxt('test01.out', a, fmt='%f')
except Exception as e:
    print(f"Lỗi: {e}")
