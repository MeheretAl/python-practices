from random import shuffle

def linear():
    #generate a list of numbers from 1 to 100
    my_list = [value for value in range(1,101)]
    #shuffle the list
    shuffle(my_list)
    print(my_list)
    target = 78

    #get the middle point
    mid = int((my_list[0] + my_list[-1])/2)
    print

    for value in range(0,len(my_list)+1):
        if value > target:
            print(value)
            mid = int(mid*3/2)
            print(mid)
        elif value < target:
            print(value)
            mid = int(mid -mid/2)
        else:
            print(value)
            print("Found it")
            break

linear()

