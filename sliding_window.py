def sliding_window(arr,k):
    i=0
    j =len(arr)
    max_number=float("-inf")
    while k <= j:
        new_array=arr[0+i:k]
        new_array=sum(new_array)
        max_number=max(new_array,max_number)
        i+=1
        k+=1

    return max_number

arr=[1,2,3,4,5,6]
k=2
new=sliding_window(arr,k)
print(new)
