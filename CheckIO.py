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
# def triangles(max):
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

# Monkey Typing
import re
def count_words(text: str, words: set) -> int:
    text = text.lower()
    result_list = []
    for word in words:
        if word in text:
            result_list.append(word)   
    return len(result_list)


print(count_words("ab cd",["abc"]))


