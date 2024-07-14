import random
import time

def merge(arr, temp_arr, left, mid, right):
    i = left    # Starting index for left subarray
    j = mid + 1 # Starting index for right subarray
    k = left    # Starting index to be sorted

    # Conditions are checked to ensure that i doesn't exceed mid and j doesn't exceed right
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            j += 1
        k += 1

    # Copy the remaining elements of left subarray, if any
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of right subarray, if any
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy the sorted subarray into the original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

def merge_sort(arr, temp_arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, temp_arr, left, mid)
        merge_sort(arr, temp_arr, mid + 1, right)
        merge(arr, temp_arr, left, mid, right)

def sort_array(arr):
    temp_arr = [0] * len(arr)
    merge_sort(arr, temp_arr, 0, len(arr) - 1)
    return arr

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_execution_time(array_size):
    arr = generate_random_array(array_size)
    start_time = time.time()
    sorted_arr = sort_array(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Example usage:
array_sizes = [100, 1000, 5000, 10000, 20000]

for size in array_sizes:
    execution_time = measure_execution_time(size)
    print(f"Execution time for sorting an array of size {size}: {execution_time:.6f} seconds")
