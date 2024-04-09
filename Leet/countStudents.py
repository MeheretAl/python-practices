def countStudents(students: list[int], sandwiches: list[int]) -> int:
    circle_lovers = students.count(0)
    square_lovers = students.count(1)

    for sandwich in sandwiches:
        if sandwich == 0:
            if circle_lovers == 0:
                return square_lovers
            circle_lovers -= 1
        else:
            if square_lovers == 0:
                return circle_lovers
            square_lovers -= 1

    return 0
