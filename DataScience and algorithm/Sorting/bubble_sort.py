#Time Complexity: O(n²) in the worst and average case, where n is the number of elements in the list.
#Space Complexity: O(1) because it sorts in place.
#Bubble Sort is simple but inefficient for large lists.


def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr[j], arr[j + 1])
    return arr

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Input array:", arr)
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)