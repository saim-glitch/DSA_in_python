def How_many_vowels(str):
    count=0
    for item in str:
        if item not in {"a","e","i","o","u"}:
            count +=1
        
        else:
            count=count
        
    return count


str="programming"
occ=How_many_vowels(str)
print(occ)