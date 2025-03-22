def generate_subbarray(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            print(arr[i:j+1])
    
        

arr=[1,2,3,4,5,6,7,8,9]
new=generate_subbarray(arr)
print(new)