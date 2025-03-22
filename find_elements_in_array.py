def find_element_in_array(arr,tar):
    arr=sorted(arr)
    n=len(arr)-1
    if tar > arr[n//2]:
            print(f"Present at index  ,{arr.index(tar)}")

    else:
            print(f"present at index , {arr.index(tar)}")


arr=[1,2,3,4,5,6,7]
tar=6
new=find_element_in_array(arr,tar)
print(new)
        