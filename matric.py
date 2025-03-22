def secondary_diag(mat):
    i=0
    j=len(mat)-1
    sc_diag=0
    while j>=0 and i < len(mat):
        sc_diag += mat[i][j]
        j -=1
        i +=1
    return sc_diag


mat=[[1,2,3],[3,6,9],[6,4,2]]
print(secondary_diag(mat))

