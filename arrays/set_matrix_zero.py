def set_matrix_zero(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    row_mat = [0]*row_len
    col_mat = [0]*col_len
    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] == 0:
                row_mat[i] = 1
                col_mat[j] = 1
    for i in range(row_len):
        for j in range(col_len):
            if row_mat[i] == 1 or col_mat[j] == 1:
                matrix[i][j] = 0
    print(matrix)








matrix = [[1,2,3],[4,0,6],[7,8,9]]
set_matrix_zero(matrix)