


def finder(matrix:list[list[int]]) -> int:
    return max([sum(i) for i in matrix])


matrix = [[1,2,3],[3,2,1],[4,5,6],[5,7,200],[6,5,7,4]]

print(finder(matrix))
