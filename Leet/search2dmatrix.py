def search2dMatrix(matrix:list[list[int]],target:int) -> bool:
        arr = []
        for i in matrix:
            for j in i:
                arr.append(j)
        #there is a better way to do this with binary search on the 2D matrix itself
        #i just converted the 2D matrix into a one dimensional array then searched through that list
        return False if target not in arr else True