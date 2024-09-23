def hoare_partition(arr, low, high):
    # Choose the pivot element (usually the first element in Hoare's partition)
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        # Find the first element greater than or equal to the pivot from the left
        i += 1
        while arr[i] < pivot:
            i += 1

        # Find the first element smaller than or equal to the pivot from the right
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If two pointers meet, return the partition index
        if i >= j:
            return j

        # Swap elements at i and j to maintain partitioning
        arr[i], arr[j] = arr[j], arr[i]

def quicksort(arr, low, high):
    if low < high:
        # Get the partition index using Hoare's partitioning
        p = hoare_partition(arr, low, high)
        
        # Recursively sort the two halves
        quicksort(arr, low, p)
        quicksort(arr, p + 1, high)

# Example usage
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Original array:", arr)
    quicksort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)