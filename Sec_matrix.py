def Diag_matrix_sum(mat):
    n=len(mat)
    matrix=0
    for i in range(n):
        
        for j in range(n):
            if i == j:
                matrix+=mat[i][j]

        for j in range(len(mat[i])