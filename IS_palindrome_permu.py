def is_palindrome_permut(str):
    dict={}
    for char in str:
        dict[char]=dict.get(char,0)+1

    count=0
    for key,val in dict.items():
        if val %2 != 0:
            count +=1

    return count <=1


str="civic"
new=is_palindrome_permut(str)
print(new)