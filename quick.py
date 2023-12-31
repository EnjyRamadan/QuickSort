def quicksort(arr, low, high):
    if low < high:
        # Find the partition index such that elements on the left are smaller,
        # and elements on the right are larger
        pi = partition(arr, low, high)

        # Recursively sort the sub-arrays
        quicksort(arr, low, pi)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    # Choose the pivot as the middle element
    pivot = arr[(low + high) // 2]

    # Initialize pointers
    i = low - 1 
    j = high + 1

    while True:
        # Find element on the left that is greater than or equal to the pivot
        i += 1
        while arr[i] < pivot:
            i += 1

        # Find element on the right that is less than or equal to the pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If pointers meet, the partitioning is complete
        if i >= j:
            return j

        # Swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]

# Example usage
if __name__ == "__main__":
    # Input array
    arr = [12, 4, 5, 6, 7, 3, 1, 15]

    # Print the original array
    print("Original array:", arr)

    # Perform quicksort
    quicksort(arr, 0, len(arr) - 1)

    # Print the sorted array
    print("Sorted array:", arr)
