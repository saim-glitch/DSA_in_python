def custom_insert(index, value, arr):
    # Validate the index
    if index < 0 or index > len(arr):
        raise ValueError("Index out of bounds")

    # Split the array into two parts
    first_part = arr[:index]
    second_part = arr[index:]

    # Insert the value and combine the parts
    result = first_part + [value] + second_part
    return result

# Example usage
arr = [1, 2, 2, 3, 4, 5, 6, 7, 9]
index = 4
value = 10
new_arr = custom_insert(index, value, arr)
print("Original array:", arr)
print("Modified array:", new_arr)
