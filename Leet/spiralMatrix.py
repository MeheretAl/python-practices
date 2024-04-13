def spiralMatrix(matrix: list[list[int]]) -> list[int]:
    left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)
    '''
    [1,2,3]
    [4,5,6]
    [7,8,9]
    '''

    answer = []
    while left < right and top < bottom:
        # from top left to top right
        for i in range(left, right):
            answer.append(matrix[top][i])
        top += 1

        # from top to bottom
        for i in range(top, bottom):
            answer.append(matrix[i][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break

        # from bottom right to bottom left
        for i in range(right - 1, left - 1, -1):
            answer.append(matrix[bottom - 1][i])
        bottom -= 1
        # from bottom to top
        for i in range(bottom - 1, top - 1, -1):
            answer.append(matrix[i][left])

        left += 1

    return answer


mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [7, 8, 9, 10]]
print(spiralMatrix(mat))
