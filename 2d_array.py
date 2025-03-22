mat=[[1,2,3],[5,6,7],[3,6,9]]
for i in range(len(mat)):
    for j in range(0,len(mat[i])):
        print(mat[i][j], end="    ")

    print(   )


for row in mat:
    for col in row:
        print(col ,  end=" ")

    print() 