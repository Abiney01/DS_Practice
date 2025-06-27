def spiral_matrix(matrix):
    top = 0
    bottom = len(matrix)
    left = 0
    right = len(matrix[0])
    result = []
    while top < bottom and left < right:
        # left to right (top)   
        for i in range(left,right):
            result.append(matrix[top][i])
        top+=1
        # right column
        for i in range(top,bottom):
            result.append(matrix[i][right-1])
        right-=1
        # right to left (bottom)
        if top < bottom:
            for i in range(right-1,left-1,-1):
                result.append(matrix[bottom-1][i])
            bottom-=1
        # left column 
        if left < right:
            for i in range(bottom-1,top-1,-1):
                result.append(matrix[i][left])
            left+=1
    return " ".join(map(str,result))
        
        

matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
print(spiral_matrix(matrix))

