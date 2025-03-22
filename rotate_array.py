def rotate_array(index,arr):
    if index==0:
        return arr
    elif index >0 and index <= len(arr)-1:    
        first=arr[:index]
        last=arr[index:]
        return last + first
    else:
        raise ValueError("Index is out of bound")
    

ind=7
array=[1,3,4,5,5,6,7,7]
rotate=rotate_array(ind,array)
print(rotate)
    