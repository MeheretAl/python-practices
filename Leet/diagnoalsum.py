def diagnoalsum(matrix:list[list[int]]) ->int:
    rowlen = len(matrix) 
    collen = len(matrix[0])
    leftadd = 0
    rightadd = 0

    for i in range(min(rowlen,collen)):
        leftadd += (matrix[i][i]) if i != min(rowlen,collen) // 2 else 0
        rightadd += (matrix[i][rowlen-1-i])


    return leftadd+rightadd


    
matrix =[[1,2,3],[4,5,6],[7,8,9]]

print(diagnoalsum(matrix))
