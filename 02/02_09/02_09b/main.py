def find_second_smallest(my_list):
    tmpList = sorted(my_list)
    return tmpList[1]

print(find_second_smallest([5, 8, 3, 2, 6]))
