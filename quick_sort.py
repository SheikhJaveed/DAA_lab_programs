def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # Choose the first element as pivot
    left = [x for x in arr[1:] if x <= pivot]  # Elements less than or equal to pivot
    right = [x for x in arr[1:] if x > pivot]  # Elements greater than pivot

    return quick_sort(left) + [pivot] + quick_sort(right)

def main():
    # Take user input for the array to be sorted
    user_input = input("Enter the numbers to be sorted, separated by spaces: ")
    unsorted_numbers = list(map(int, user_input.split()))

    sorted_numbers = quick_sort(unsorted_numbers)
    print("Sorted numbers:", sorted_numbers)

if __name__ == "__main__":
    main()
