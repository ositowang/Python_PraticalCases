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


# # Even the last 

# def checkio(array):
#     """
#         sums even-indexes elements and multiply at the last
#     """
#     if len(array) == 0:
#         return 0 
#     sum = 0 
#     for x in range(0,len(array)):
#         if x%2 == 0:
#             sum += array[x] 
#     return sum*array[-1]

# #These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
#     assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
#     assert checkio([6]) == 36, "(6)*6=36"
#     assert checkio([]) == 0, "An empty array = 0"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


# def checkio(words: str) -> bool:
#     words_list = words.split()
#     count = 0
#     for i in words_list:
#         if i.isalpha():
#             count += 1
#             if count >= 3:
#                 return True
#         else:
#             count = 0
#     return False
    

# #These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio("Hello World hello") == True, "Hello"
#     assert checkio("He is 123 man") == False, "123 man"
#     assert checkio("1 2 3 4") == False, "Digits"
#     assert checkio("bla bla bla bla") == True, "Bla Bla"
#     assert checkio("Hi") == False, "Hi"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


# import re 
# def left_join(phrases):

#     """
#         Join strings and replace "right" to "left"
#     """
#     result_string =",".join(phrases)
#     result_string = re.sub("right","left",result_string)
#     return result_string

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
#     assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
#     assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
#     assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# #Number Base 
# def checkio(str_number: str, radix: int) -> int:
    
#     return -1

# #These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio("AF", 16) == 175, "Hex"
#     assert checkio("101", 2) == 5, "Bin"
#     assert checkio("101", 5) == 26, "5 base"
#     assert checkio("Z", 36) == 35, "Z base"
#     assert checkio("AB", 10) == -1, "B > A = 10"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")