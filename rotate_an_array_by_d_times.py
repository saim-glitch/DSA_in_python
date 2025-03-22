# def reverse_an_array_by_d_times(d,arr):
#     i=0
#     d=d-1
#     while i<=d:
#         arr.append(arr[0])
#         arr.pop(0)
#         i+=1
#     return arr


# d=8
# arr=[1,2,3,4,5,6,7,8]
# new=reverse_an_array_by_d_times(d,arr)
# print(new)


def rotate_an_array(d,arr):
    n=len(arr)
    if d > n:
        d=d%n
    else:
        for i in range(d):
            temp=arr[0]
            for j in range(n):
                arr[j]=arr[j+1]
            arr[i-1]=temp


d=8
arr=[1,2,3,4,5,6,7,8]
new=rotate_an_array(d,arr)
print(new)