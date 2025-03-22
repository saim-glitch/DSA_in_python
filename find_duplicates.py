def find_duplicates(str):
    s=[]
    for key,val in str:
        if val > 2:
            s.append(key)
        return val  
    

str = ""