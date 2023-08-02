#Python3 Code @BritoAlv

def gaussian_elimination(matrix):
    number_columns = len(matrix)
    for i in range(0, number_columns-1):
        matrix = stage_gaussian_elimination(matrix, i)
    return matrix    

def stage_gaussian_elimination(matrix, stage):
    # stage represents the column of the matrix that we want to zero out elements below diagonal.
    # matrix should be an nxn matrix.
    for i in range(stage+1, len(matrix)): # move along rows
        for j in range(0, len(matrix)): # move along columns.
            matrix[i][j] = matrix[i][j] - ( matrix[i][stage]/ matrix[stage][stage])*matrix[stage][j] 
    return matrix

matrix = [
            [3,2,1],
            [1,1,1],
            [1,1,0]
         ]         
matrix = gaussian_elimination(matrix)
print(matrix[0])
print(matrix[1])
print(matrix[2])

    
