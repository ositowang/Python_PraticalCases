# """
# This file includes the basic and most common algorithm in computer science
# written in Python with possible explanations and better solutions 

# """

# # Binary Search 
# def binary_search(item,data) -> int:
#     """
#     Binary search compares the target value to the middle element of the array; if they are unequal, 
#     the half in which the target cannot lie is eliminated and the search continues on the remaining half until it is successful. 
#     If the search ends with the remaining half being empty, the target is not in the array.
#     complexity is log(len(data))
#     Note: The input list must be a sorted list
#     """
#     low = 0
#     high = len(data)-1
#     while low <= high:
#         middle = (low+high)//2
#         guess = data[middle]
#         if item >guess:
#             low = middle+1
#         elif item <guess:
#             high = middle-1
#         else:
#             return middle 
#     return None

# my_list = [1,3,5,7,9]
# print(binary_search(3,my_list))


# D&C
"""
分治算法的基本原理：
	1. 找出最简单的基线条件
    2. 确定如何缩小问题的规模，使其符合基线条件
"""
# # Find the length

# def find_length_recursion(data):
#     if len(data) == 0:
#         return 0
#     else:
#         return 1+find_length_recursion(data[1:])

# print(find_length_recursion([1,2,3,4,5,6,7,8,8,9,10]))


# Find the largest 

# def find_the_largetst(data):
#     if len(data)==1:  
#         return data[0]  
#     return data[0] if data[0]>find_the_largetst(data[1:]) else find_the_largetst(data[1:])  

# print(find_the_largetst([1,2,3,4,7,10,22]))


# Dividing the rectangle

# def dividing_rectangle(a,b):
#     if a%b==0:
#         return a if a<b else b
#     return dividing_rectangle(a,a%b) if a > b else dividing_rectangle(b,b%a)

# print(dividing_rectangle(1680,640))

# # Quick Sort

# def quick_sort(array):
#     if len(array)<2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i >pivot]
#         return quick_sort(less)+[pivot]+quick_sort(greater)

# print(quick_sort([10,5,2,3]))


# Breadth-First Search

# Pseudo Code
from collections import deque
search_deque = deque()
search_deque += graph["you"]
searched = []
while search_deque:
    person = search_deque.popleft()
    if person not in searched:
        if person_is_seller(person):
            print(person)
        else:
            search_deque += graph[person]
            searched.append(person)
return False


# 狄克斯特拉算法

#example code 

node = find_lowest_cost_node(costs)  # Find the node with lowest cost
while node is not None:              # the loop stops after all the nodes are processed 
    cost = cost[node]                
    neighbors = graph[node]
    for n in neighbors.keys():        #Check all the neighbors of the current node
        new_cost = cost + neighbors[n]  
        if cost[n] > new_cost:         # if the cost is lowers by driving through the current nodes to the neighbors 
            costs[n] = new_cost        # Update the cost of the neighbors 
            parents[n] = node          # Set the current neighbor's parent node as the current node
    processed.append(node)             # Push the current node into processed 
    node = find_lowest_cost_node(costs) # loop through all the nodes 
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # if the node with lower cost and not been processed before
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node