# def checkio(data):
#     ROMANS = (('M',  1000),
#           ('CM', 900),
#           ('D',  500),
#           ('CD', 400),
#           ('C',  100),
#           ('XC', 90),
#           ('L',  50),
#           ('XL', 40),
#           ('X',  10),
#           ('IX', 9),
#           ('V',  5),
#           ('IV', 4),
#           ('I',  1))
#     result = ""
#     for roman,value in ROMANS:
#         while data >= value:
#             data -= value 
#             result += roman
    
#     return result

# # Same but better solution

# def checkio(n):
#     result = ''
#     for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
#                              'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
#         result += n // arabic * roman
#         n %= arabic
#     return result

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(6) == 'VI', '6'
#     assert checkio(76) == 'LXXVI', '76'
#     assert checkio(499) == 'CDXCIX', '499'
#     assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
#     print('Done! Go Check!')

# # Find Sequence clearest solution

# def  checkiocheckio((matrixmatrix))::
#         NN  ==  lenlen((matrixmatrix))
#         defdef  seq_lenseq_len((xx,,  yy,,  dxdx,,  dydy,,  numnum))::
#                 if 0 <= x < N and 0 <= y < N and matrix[y][x] == num:
#             return 1 + seq_len(x + dx, y + dy, dx, dy, num)
#         else:
#             return 0

#     DIR = [(dx, dy) for dy in range(-1, 2)
#                     for dx in range(-1, 2)
#                     if dx != 0 or dy != 0]
#     for y in range(N):
#         for x in range(N):
#             for dx, dy in DIR:
#                 if seq_len(x, y, dx, dy, matrix[y][x]) >= 4:
#                     return True
#     return False

# Hamming distance

# def checkio(n, m):
#     bin_n = bin(n)
#     bin_m = bin(m)
#     print(len(bin_m),len(bin_n))
#     print(bin_m.zfill(len(bin_n)))
#     result = 0 
#     if len(bin_m)>len(bin_n):
#         bin_n = bin_n.zfill(len(bin_m))
#     elif len(bin_m) < len(bin_n):
#         bin_m = bin_m.zfill(len(bin_n))
#     bin_list = list(zip([a for a in bin_m if not a.isalpha()],[b for b in bin_n if not b.isalpha()]))
#     for x in bin_list:
#         if int(x[0]) + int(x[1]) == 1:
#             result += 1
#     return result 

# # best solution
# def hammin_distance(n, m):
#     """
#     1.与运算：A与B值均为1时，A、B与的运算结果才为1，否则为0 （运算符：&）

#     2.或运算：A或B值为1时，A、B或的运算结果才为1，否则为0  （运算符：|）

#     3.异或运算：A与B不同为1时，A、B的预算结果才为1，否则为0  （运算符：^）

#     4.按位翻转(按位取反)：将内存中表示数字的2进制数取反0取1，1取0 （运算符：~）
#     """
#     return bin(n ^ m).count('1')
    
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(117, 17) == 3, "First example"
#     assert checkio(1, 2) == 2, "Second example"
#     assert checkio(16, 15) == 5, "Third example"


# # Parensis Check
# def checkio(expression):
#     # 存储左括号和右括号
#     open_brackets = '([{<'
#     close_brackets = ')]}>'
#     # 映射左右括号便于出栈判断
#     brackets_map = {')': '(', ']': '[', '}': '{'}
#     flag = True
#     check_stack = []
#     for i in expression:
#         if i in open_brackets:
#             check_stack.append(i)
#         elif i in close_brackets:
#             if len(check_stack) == 0:
#                 flag = False
#                 break
#             elif brackets_map[i] == check_stack[-1]:
#                 check_stack.pop()
#             else:
#                 flag = False
#                 break
#         else:
#             continue 
#     if check_stack != []:
#         flag = False
#     return flag

# # Better Solution
# def checkio_better(data):
#     """
#     solved the pop from empty list by adding a empty element

#     """
#     stack=[""]
#     brackets={"(":")","[":"]","{":"}"}
#     for c in data:
#         if c in brackets:
#             stack.append(brackets[c])
#         elif c in brackets.values() and c!=stack.pop():
#             return False
#     return stack==[""]

# if __name__ == '__main__':
#     assert checkio("((5+3)*2+1)") == True, "Simple"
#     assert checkio("{[(3+1)+2]+}") == True, "Different types"
#     assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
#     assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
#     assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
#     assert checkio("2+3") == True, "No brackets, no problem"


# # Restricted Sums
# """
# Our new calculator is censored and as such it does not accept certain words. You should try to trick by writing a program to calculate the sum of numbers.

# Given a list of numbers, you should find the sum of these numbers. Your solution should not contain any of the banned words, even as a part of another word.

# The list of banned words are as follows:

# sum
# import
# for
# while
# reduce
# Input: A list of numbers.

# Output: The sum of numbers.
# """
# # Using Recursion
# def checkio(data):
#     try:
#         return checkio(data[1:])+data[0]
#     except IndexError:
#         return 0 

# # Not good solutions

# def checkio_eval(data):
#     d = map(str, data)
#     return eval('+'.join(d))

# 经典的回文算法问题

# 暴力破解法，我就会这个
# def longest_palindromic(text):
#     if not text:
#         return ""

#     n = len(text)
#     longest, left, right = 0, 0, 0
#     for i in range(0, n):
#         for j in range(i + 1, n + 1):
#             substr = text[i:j]
#             if isPalindrome(substr) and len(substr) > longest:
#                 longest = len(substr)
#                 left, right = i, j
#     # construct longest substr
#     result = text[left:right]
#     return result

# def isPalindrome(text):
#     if not text:
#         return False
#     # reverse compare
#     return text == text[::-1]

# if __name__ == '__main__':
#     assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
#     assert longest_palindromic("abacada") == "aba", "The First"
#     assert longest_palindromic("aaaa") == "aaaa", "The A"



# # Number Factory

# """
# You are given a two or more digits number N. For this mission, 
# you should find the smallest positive number of X, such that the product of its digits is equal to N. 
# If X does not exist, then return 0.
# """
# import functools

# def checkio(number):
#     """
#     Return the smallest integer such that the product of its digits equal 'number'.
#     If this is not possible, return zero.
#     """
#     # Special case for one to keep the logic simpler (and zero, as an early out).
#     if number <= 1:
#         return number

#     # Factor number into factors in the range [2, 9] (inclusive)
#     factors = []
#     for d in reversed(range(2, 10)):
#         while number > 1 and not number % d:
#             print(number)
#             number //= d
#             print(number)
#             factors.append(d)
            
#     # If the number has not been completely factored, it must have prime
#     # factors larger than seven.  In this case, it's impossible to factor
#     # with digits, so return zero.
#     if number > 1:
#         return 0
    
#     # Combine the factors back into a single integer.
#     # Use reversed so that smaller digits come first.
#     return functools.reduce(lambda a, b: 10 * a + b, reversed(factors))

# Biggest Rectangle

def largest_histogram(histogram):
    area_list = []
    for i in range(0,len(histogram)):  # Loop through the list
        n = 0
        height_list = [histogram[i]] 
        while i+n<len(histogram):           
            height_list.append(histogram[i+n])
            area_list.append(min(height_list)*(1+n))
            n +=1 
    return max(area_list)


# With the same logic but more pythonic
def largest_histogram_better(histogram):
    n = len(histogram)
    return max((j - i) * min(histogram[i:j]) for i in range(n) for j in range(i+1, n+1))

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")

