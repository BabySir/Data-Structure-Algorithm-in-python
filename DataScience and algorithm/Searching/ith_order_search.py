#Average case: O(n)
#Worst case: O(n²) (happens rarely due to randomization)


import random

# Partition function similar to QuickSort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Randomized partition to ensure expected O(n) time complexity
def randomized_partition(arr, low, high):
    rand_pivot = random.randint(low, high)
    arr[high], arr[rand_pivot] = arr[rand_pivot], arr[high]
    return partition(arr, low, high)

# QuickSelect function to find the k-th smallest element
def quickselect(arr, low, high, k):
    if low <= high:
        # Get the position of the randomly partitioned pivot
        pivot_index = randomized_partition(arr, low, high)
        
        # If pivot_index is k, then we've found the k-th smallest element
        if pivot_index == k:
            return arr[pivot_index]
        
        # If pivot_index is greater than k, search in the left part
        elif pivot_index > k:
            return quickselect(arr, low, pivot_index - 1, k)
        
        # If pivot_index is less than k, search in the right part
        else:
            return quickselect(arr, pivot_index + 1, high, k)
    
    return None

# Function to find the nth smallest element
def nth_smallest(arr, n):
    return quickselect(arr, 0, len(arr) - 1, n - 1)

# Function to find the nth largest element
def nth_largest(arr, n):
    return quickselect(arr, 0, len(arr) - 1, len(arr) - n)

# Example usage
if __name__ == "__main__":
    arr = [12, 3, 5, 7, 19, 1, 18]
    n = 3
    
    print(f"The {n}-th smallest element is: {nth_smallest(arr, n)}")
    print(f"The {n}-th largest element is: {nth_largest(arr, n)}")