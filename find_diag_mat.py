mat=[[1,2,3],[6,8,3],[9,5,2]]

def find_dia_mat(mat):
    pd_diag=0
    sec_diag=0
    n=len(mat)
    for i in range(n):
        pd_diag += mat[i][i]
        sec_diag += mat[i][n-1-i]

    print(f"principal diagnal sum is {pd_diag}")
    print(f"secondary diagnal sum is {sec_diag}")

diagnal=find_dia_mat(mat)
print(diagnal)