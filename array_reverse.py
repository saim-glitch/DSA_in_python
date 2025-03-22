# def array_reverse(arr):
#     lst=[]
#     for i in range(len(arr)-1,-1,-1):
#         lst.append(arr[i])

# print(lst)
# arr=[1,2,3,4,5,6,7,8,9,10]
# new=array_reverse(arr)
# print(new)


# def reverse_array(arr):
#     length=len(arr)//2
#     first=arr[:length][::-1]
#     second=arr[length:][::-1]
#     full_reversed=second+first
#     return full_reversed

# arr=[1,2,3,4,5,6,7,89]
# new=reverse_array(arr)
# print(new)


def reverse_array(arr):
    i=0
    j=len(arr)-1
    while i<=j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

    return arr

arr=[1,2,3,4,5,6,7,8,9]
new=reverse_array(arr)
print(new)