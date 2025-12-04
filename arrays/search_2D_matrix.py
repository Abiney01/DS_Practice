def searchMatrix(matrix, target):
        row = len(matrix)
        col = len(matrix[0])
        top = 0
        bottom = row-1
        while top<=bottom:
            row = (top+bottom)//2
            if matrix[row][-1] < target:
                top = row+1
            elif matrix[row][0] > target:
                bottom = row-1
            else:
                break
        if not(top<=bottom):
            return False
        left = 0
        right = col-1
        while left<=right:
            mid = (left+right)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left+=1
            else:
                right-=1
        return False

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10

print(searchMatrix(matrix,target))