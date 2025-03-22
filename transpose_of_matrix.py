mat=[[1,2,4],
     [3,4,5],
     [9,10,3]]

def transpose_mat(mat):
    for i in range(len(mat)):
        for j in range(i+1,len(mat[0])):
                temp=mat[i][j]
                mat[i][j]=mat[j][i]
                mat[j][i]=temp
    print(mat, end="   ")
    print()

diag=transpose_mat(mat)
print(diag)


def trans(mat):
    for i in range(len(mat)):
          for j in range(i+1,len(mat[0])):
               mat[i][j],mat[j][i]=mat[j][i],mat[i][j]


    return mat