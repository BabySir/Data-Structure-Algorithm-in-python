#This algorithm has a time complexity of O(n²) 



def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Assume the minimum element is the first element in the unsorted part
        min_idx = i
        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Example usage:
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)