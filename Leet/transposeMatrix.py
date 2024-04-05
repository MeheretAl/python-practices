def transpose(matrix:list[list[int]]) -> list[list[int]]:
    rows = len(matrix)
    columns = len(matrix[0])
    #newMatrix = [[0] * rows for x in range(columns) ]
    newMatrix = []
    #creating the transpose matrix
    for i in range(columns):
        row = []
        for j in range(rows):
            row.append(0)
        newMatrix.append(row)

    #populating the transpose matrix with the correct values
    for i in range(rows):
        for j in range(columns):
            newMatrix[j][i] = matrix[i][j]

    return newMatrix
