#Best case: O(n) (when the array is already sorted).
#Worst and Average case: O(n²) (when the array is sorted in reverse order).

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place key at its correct position
        arr[j + 1] = key
    
    return arr

# Example usage:
arr = [12, 11, 13, 5, 6,88]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)