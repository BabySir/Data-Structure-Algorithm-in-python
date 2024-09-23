#Best and Average case: O(n log n)
#Worst case: O(n²) (when the pivot is always the smallest or largest element).

def partition(arr, low, high):
    # Choose the rightmost element as pivot
    pivot = arr[high]
    
    # Pointer for greater element
    i = low - 1

    # Traverse through all elements and compare them with the pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            # If an element is smaller than or equal to pivot, swap it with the element at i
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the partitioning index
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        # Find the partitioning index
        pi = partition(arr, low, high)
        
        # Recursively sort the elements before and after the partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("Sorted array:", arr)