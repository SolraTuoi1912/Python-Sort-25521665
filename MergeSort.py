import numpy as np
import time

a = np.loadtxt('test01.inp', dtype = float)
b = np.array(a)

def merge_sort(l, r):
    if l == r:
        return
    mid = (l + r) // 2
    merge_sort(l, mid)
    merge_sort(mid + 1, r)
    vtl = l
    vtr = mid + 1
    vt = l
    while vt <= r:
        if (vtl <= mid and vtr <= r):
            if (a[vtl] <= a[vtr]):
                b[vt] = a[vtl]
                vtl += 1
            else:
                b[vt] = a[vtr]
                vtr += 1
        else:
            if (vtl <= mid):
                b[vt] = a[vtl]
                vtl += 1
            else:
                b[vt] = a[vtr]
                vtr += 1
        vt += 1
    a[l : r + 1] = b[l : r + 1]
    return

start_time = time.perf_counter()
merge_sort(0, a.size - 1)
end_time = time.perf_counter()

np.savetxt('test01.out', a, fmt='%f')
print("Time:",end_time - start_time, 's')
