def find_dup_in_subarr(arr,k):
    i=0
    j=len(arr)
    new_array=[]
    while k <= j:
        new_array=arr[0+i:k]
        for L in range(0,len(new_array)-1):
            for M in range(L+1,len(new_array)):
                if new_array[L]==new_array[M]:
                    return True
                
            i+=1
            k+=1
        return False

arr=[1,2,3,4,5,6,6]
k=3
new=find_dup_in_subarr(arr,k)
print(new)