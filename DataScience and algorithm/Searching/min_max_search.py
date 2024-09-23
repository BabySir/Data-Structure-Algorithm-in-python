def min_max_search(arr):
    n = len(arr)
    # Traverse through all array elements
    min=arr[0]
    max=arr[1]
    if min>max:
        min,max=max,min

    for i in range(2,n):
        # Last i elements are already in place
        if max < arr[i]:
            max=arr[i]
        if min > arr[i]:
            min =arr[i]
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element    
    return min,max

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]

print("Input array:", arr)
print(min_max_search(arr))