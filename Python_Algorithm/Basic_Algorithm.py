"""
This file includes the basic and most common algorithm in computer science
written in Python with possible explanations and better solutions 

"""

# Binary Search 
def binary_search(item,data) -> int:
    """
    Binary search compares the target value to the middle element of the array; if they are unequal, 
    the half in which the target cannot lie is eliminated and the search continues on the remaining half until it is successful. 
    If the search ends with the remaining half being empty, the target is not in the array.
    complexity is log(len(data))
    Note: The input list must be a sorted list
    """
    low = 0
    high = len(data)-1
    while low <= high:
        middle = (low+high)//2
        guess = data[middle]
        if item >guess:
            low = middle+1
        elif item <guess:
            high = middle-1
        else:
            return middle 
    return None

my_list = [1,3,5,7,9]
print(binary_search(3,my_list))