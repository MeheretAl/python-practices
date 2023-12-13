def smaller(list1:list[int]) -> list[int]:
    counter = []
    count = 0
    for i in range(len(list1)):
        count = 0
        for j in range(len(list1)):
            if list1[i] > list1[j]:
                count+=1
        counter.append(count)

    return counter

smaller([8,1,2,2,3])

