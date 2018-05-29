# Bubble sort


def bubble_sort(list):
    for index in range(len(list)):
        for i in range(1, len(list) - index):
            if list[i - 1] > list[i]:
                list[i - 1], list[i] = list[i], list[i - 1]
    return list


# A better bubble sort

def bubble_sort_better(list):
    for index in range(len(list)):
        flag = True
        for i in range(1, len(list) - index):
            if list[i - 1] > list[i]:
                list[i - 1], list[i] = list[i], list[i - 1]
                flag = False
        if flag:
            return list
    return list

#Selection Sort

def selection_sort(arr):
    new_array = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_array.append(arr.pop(smallest))
    return new_array

# Helper function

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in (0,len(arr)):
        if smallest < arr[i]:
            smallest = arr[i]
            smallest_index = i 
    return smallest_index
