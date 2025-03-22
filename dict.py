def find_seq(str):
    dc={}
    for char in str:
        if char in dc:
            dc[char]=dc[char]+1
        else:
            dc[char]=dc[char]
    return dc

str="programming"
new_dict=find_seq(str)
print(new_dict)