def transpose_matrix(matrix):
    result = [[0]*len(matrix) for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result

matrix = [[1,2,3],[4,5,6]]
print(transpose_matrix(matrix))