# import re

# # My Solution 
# def checkio(data: str) -> bool:
#     match_pat = re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{10,}$",data)
#     if match_pat:
#         return True
#     else:
#         return False






# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio('A1213pokl') == False, "1st example"
#     assert checkio('bAse730onE4') == True, "2nd example"
#     assert checkio('asasasasasasasaas') == False, "3rd example"
#     assert checkio('QWERTYqwerty') == False, "4th example"
#     assert checkio('123456123456') == False, "5th example"
#     assert checkio('QwErTy911poqqqq') == True, "6th example"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


# # Solution 1, My solution with many strip,replace and substitute
# import string
# import re
# def checkio(text: str) -> str:
#     text = text.replace(' ','')
#     text = text.lower()
#     text = re.sub(r"[\s+\.\!\/_,$%^*(+\"\'0-9]",'',text)
#     dict = {i:text.count(i) for i in text}
#     frequency = [i for i in dict.values() ]
#     most_frequent = [a for a in dict if dict[a]==max(frequency)]
#     return min(most_frequent)

# # My optimized solution with isalpha() to save the strip and replacements

# def better_solutions(text: str) -> str:
#     text = text.lower()
#     dict = {i:text.count(i) for i in text if i.isalpha()}
#     frequency = [i for i in dict.values() ]
#     most_frequent = [a for a in dict if dict[a]==max(frequency)]
#     return min(most_frequent)



# # Solution 3, the most concise solution I have ever seen
# def best_solution(text: str) -> str:
#     text = text.lower()
#     return max(string.ascii_lowercase, key=text.count)

 
# print(checkio("Lorem ipsum dolor sit amet 0000000000000000000"))


# Generator for Triangles 
# def triangles(i):
#     result_list = [1]
#    while True:
#         yield result_list
#         result_list = [1]+[result_list[i]+result_list[i+1] for i in range(len(result_list)-1)]+[1]
    

# # Non-Unique Elements 
# def checkio(data: list) -> list:
#     result_list = []
#     for element in data:
#         if data.count(element)>1:
#             result_list.append(element)
#     return result_list

# if __name__ == "__main__":
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
#     assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
#     assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
#     assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
#     print("It is all good. Let's check it now")

# # Monkey Typing
# import re
# def count_words(text: str, words: set) -> int:
#     text = text.lower()
#     result_list = []
#     for word in words:
#         if word in text:
#             result_list.append(word)   
#     return len(result_list)

# # Better Solutions
# def count_words(text, words):
#     return sum(w in text.lower() for w in words)


# # Xs and Os  Referre
# from typing import List
# def checkio(result):
#     rows = result
#     cols = map(''.join, zip(*rows))
#     # enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.
#     diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
#     lines = rows + list(cols) + list(diags)
#     return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'

# #Pawn Brotherhood
# def safe_pawns(pawns: set) -> int:
#     pawn_coord = []
#     count = 0
#     for pawn in pawns:
#         hori_coord = ord(pawn[0])-97
#         verti_coord = int(pawn[1])
#         pawn_coord.append((hori_coord,verti_coord))
#     for hori_coord,verti_coord in pawn_coord:
#         print(hori_coord,verti_coord)
#         if ((hori_coord-1,verti_coord-1) in pawn_coord) or ((hori_coord+1,verti_coord-1) in pawn_coord):
#             count+=1
#     return count
    
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
#     assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

#Long Repeat
def long_repeat(line):
    """
    At first, I was stuck in split the string by same letter and got lost.
    Then I realize I only need to count the number, if same letter stops,
    I only need to restart the count from beginning
    """
    if line == "":
        return 0
    else:
        counter = 1
        result = 1
        for i in range(1,len(line)):
            if line[i] == line[i-1]:
                counter += 1
                if counter > result:
                    result = counter
            else:
                counter = 1  # if the sequece of same letter stops, then restart the counter
        return result


# Most Creative solution
from itertools import groupby
def long_repeat_best(line):
    """
    class groupby(object):
    Make an iterator that returns consecutive keys and groups from the iterable.
    [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
    """
    return max((sum(1 for _ in g) for k, g in groupby(line)), default=0)
            

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')






