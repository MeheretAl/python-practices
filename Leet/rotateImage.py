def rotate(matrix:list[list[int]]) -> None:
    #transposing the matrix here
    #we can use the upper triangular matrix i<=j 
    #or the lower triangular matrix i>=j doesn't really matter which
    #because we swap it with the lower one or the upper one depending on our choice
    size = len(matrix)
    #using size for everything becuase it is an n by n matrix
    #[[1,2,3] , [4,5,6] , [7,8,9]]
    for i in range(size):
        for j in range(size):
            if i <= j:
                matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]
    #the matrix is now [[1,4,7],[2,5,8],[3,6,9]]
    #after transposing it needs to be reversed
    for i in range(size):
        leftptr, rightptr = 0,size-1
        for j in range(size):
            while leftptr < rightptr:
                matrix[i][leftptr] , matrix[i][rightptr]= matrix[i][rightptr], matrix[i][leftptr]
                leftptr+=1
                rightptr-=1

    
            
    print(matrix)

    

matrix = [[1,2,3],[4,5,6],[7,8,9]]

rotate(matrix=matrix)