# # Difference
# def checkio(*args):
#     if len(args) == 0:
#         return "0"
#     sorted_list = sorted(args,reverse=True)
#     difference = sorted_list[0]-sorted_list[-1] 
#     return difference

# #These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     def almost_equal(checked, correct, significant_digits):
#         precision = 0.1 ** significant_digits
#         return correct - precision < checked < correct + precision

#     assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
#     assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
#     assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
#     assert almost_equal(checkio(), 0, 3), "Empty"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


# Even the last 

def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) == 0:
        return 0 
    sum = 0 
    for x in range(0,len(array)):
        if x%2 == 0:
            sum += array[x] 
    return sum*array[-1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")