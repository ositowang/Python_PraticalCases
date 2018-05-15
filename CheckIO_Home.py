# import re

# def checkio(data: str) -> bool:
#     match_pat = re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{10,}$",data)
#     if match_pat:
#         return True
#     else:
#         return False

# #Some hints
# #Just check all conditions



# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio('A1213pokl') == False, "1st example"
#     assert checkio('bAse730onE4') == True, "2nd example"
#     assert checkio('asasasasasasasaas') == False, "3rd example"
#     assert checkio('QWERTYqwerty') == False, "4th example"
#     assert checkio('123456123456') == False, "5th example"
#     assert checkio('QwErTy911poqqqq') == True, "6th example"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
import string
import re
def checkio(text: str) -> str:
    # text = text.replace(' ','')
    # text = text.lower()
    # text = re.sub(r"[\s+\.\!\/_,$%^*(+\"\'0-9]",'',text)
    # dict = {i:text.count(i) for i in text}
    # frequency = [i for i in dict.values() ]
    # most_frequent = [a for a in dict if dict[a]==max(frequency)]
    # return min(most_frequent)
    text = text.lower()
    print(text.ascii_lowercase())
    return max(string.ascii_lowercase, key=text.count)

 

print(checkio("Lorem ipsum dolor sit amet 0000000000000000000"))
