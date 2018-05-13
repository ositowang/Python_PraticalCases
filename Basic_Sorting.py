# Bubble sort


def bubble_sort(list):
    for index in range(len(list)):
        for i in range(1, len(list) - index):
            if list[i - 1] > list[i]:
                list[i - 1], list[i] = list[i], list[i - 1]
    return list


# A better bubble sort

def bubble_sort(list):
    for index in range(len(list)):
        flag = True
        for i in range(1, len(list) - index):
            if list[i - 1] > list[i]:
                list[i - 1], list[i] = list[i], list[i - 1]
                flag = False
        if flag:
            return list
    return list




