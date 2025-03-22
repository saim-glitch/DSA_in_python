def find_manual_maximum(arr, k):
    if k > len(arr):  # Ensure k is valid
        return "Error: k cannot be greater than the length of the array."
    
    result = []
    for _ in range(k):
        max_val = arr[0]  # Initialize max with the first element
        for i in range(1, len(arr)):
            if arr[i] > max_val:
                max_val = arr[i]
        arr.append(max_val)  # Add the current maximum to the result
        arr.remove(max_val)     # Remove the current maximum from the array
    
    return arr  # Return the k largest values in descending order



arr = [3, 1, 4, 1, 5, 9, 2,50]
k = 3
print(find_manual_maximum(arr, k))
