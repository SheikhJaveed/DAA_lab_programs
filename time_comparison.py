import random
import time
import matplotlib.pyplot as plt

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())
    end_time = time.time()
    return end_time - start_time


array_sizes = [100, 200, 300, 500, 1000, 2000, 3000, 5000, 6000, 8000]
merge_sort_times = []
insertion_sort_times = []
selection_sort_times = []

for size in array_sizes:
    test_array = [random.randint(0, 100000) for _ in range(size)]

    merge_sort_times.append(measure_time(merge_sort, test_array))
    insertion_sort_times.append(measure_time(insertion_sort, test_array))
    selection_sort_times.append(measure_time(selection_sort, test_array))

print("Size\tMerge Sort Time\tInsertion Sort Time\tSelection Sort Time")
for i, size in enumerate(array_sizes):
    print(f"{size}\t{merge_sort_times[i]:.6f}\t{insertion_sort_times[i]:.6f}\t{selection_sort_times[i]:.6f}")

plt.figure(figsize=(10, 6))
plt.plot(array_sizes, merge_sort_times, label='Merge Sort')
plt.plot(array_sizes, insertion_sort_times, label='Insertion Sort')
plt.plot(array_sizes, selection_sort_times, label='Selection Sort')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Performance')
plt.legend()
plt.grid(True)
plt.show()
