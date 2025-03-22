def reverse_array(arr):
    i = 0  # Start pointer
    j = len(arr) - 1  # End pointer

    while i < j:
        # Swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]
        # Move the pointers closer
        i += 1
        j -= 1

    return arr

# Example usage
arr = [1, 2, 2, 3, 4, 5, 6, 7, 9]
reversed_arr = reverse_array(arr)
print("Reversed array:", reversed_arr)
