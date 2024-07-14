# Python3 Program for recursive binary search.


# Returns index of x in arr if present, else -1
def binarySearch(arr, low, high, x):
    # Check base case
    if low<=high:

        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)


        else:
            return binarySearch(arr, mid + 1, high, x)

    else:
        return -1



arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
