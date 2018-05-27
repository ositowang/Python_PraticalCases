import re

# My Solution 
def checkio(data: str) -> bool:
    match_pat = re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{10,}$",data)
    if match_pat:
        return True
    else:
        return False






if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


# Solution 1, My solution with many strip,replace and substitute
import string
import re
def checkio(text: str) -> str:
    text = text.replace(' ','')
    text = text.lower()
    text = re.sub(r"[\s+\.\!\/_,$%^*(+\"\'0-9]",'',text)
    dict = {i:text.count(i) for i in text}
    frequency = [i for i in dict.values() ]
    most_frequent = [a for a in dict if dict[a]==max(frequency)]
    return min(most_frequent)

# My optimized solution with isalpha() to save the strip and replacements

def better_solutions(text: str) -> str:
    text = text.lower()
    dict = {i:text.count(i) for i in text if i.isalpha()}
    frequency = [i for i in dict.values() ]
    most_frequent = [a for a in dict if dict[a]==max(frequency)]
    return min(most_frequent)



# Solution 3, the most concise solution I have ever seen
def best_solution(text: str) -> str:
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

 
print(checkio("Lorem ipsum dolor sit amet 0000000000000000000"))


Generator for Triangles 
def triangles(i):
    result_list = [1]
   while True:
        yield result_list
        result_list = [1]+[result_list[i]+result_list[i+1] for i in range(len(result_list)-1)]+[1]
    

# Non-Unique Elements 
def checkio(data: list) -> list:
    result_list = []
    for element in data:
        if data.count(element)>1:
            result_list.append(element)
    return result_list

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")

# Monkey Typing
import re
def count_words(text: str, words: set) -> int:
    text = text.lower()
    result_list = []
    for word in words:
        if word in text:
            result_list.append(word)   
    return len(result_list)

# Better Solutions
def count_words(text, words):
    return sum(w in text.lower() for w in words)


# Xs and Os  Referre
from typing import List
def checkio(result):
    rows = result
    cols = map(''.join, zip(*rows))
    # enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)
    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'

#Pawn Brotherhood
def safe_pawns(pawns: set) -> int:
    pawn_coord = []
    count = 0
    for pawn in pawns:
        hori_coord = ord(pawn[0])-97
        verti_coord = int(pawn[1])
        pawn_coord.append((hori_coord,verti_coord))
    for hori_coord,verti_coord in pawn_coord:
        print(hori_coord,verti_coord)
        if ((hori_coord-1,verti_coord-1) in pawn_coord) or ((hori_coord+1,verti_coord-1) in pawn_coord):
            count+=1
    return count
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

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


# All the same 
from typing import List, Any

# My  first to mind solutions
def all_the_same(elements: List[Any]) -> bool:
    if len(elements) == 1 or not elements:
        return True
    else:
        my_list = []
        for i in range(0,len(elements)-1):
            if elements[i] == elements[i+1]:
                my_list.append(1)
            else:
                my_list.append(0)
        if 0 in my_list:
            return False
        return True

# a better solution

def all_the_same(elements: List[Any]) -> bool:
    if elements == []:
        return True
        """
        no need to create flags, take the first element, if it matches with the others return true else false
        """
    example = elements[0]
    for x in elements:
        if x != elements[0]:
            return False
    return True

# best solution

def all_the_same(elements):
    """
    very clever solution
    """
   return elements[1:] == elements[:-1]


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")


Caesar Cipher

# My straight forward solutions
def to_encrypt(text, delta):
    result_text= ""
    for x in text:
        if x.isalpha():
            x_num = ord(x)+delta
            if x_num > 123:
                new_letter = chr(x_num-26)
                result_text += new_letter
            elif x_num < 97:
                new_letter = chr(123+(x_num-97))
                result_text += new_letter
            else:
                result_text += chr(x_num)
        else:
            result_text += x
    return result_text

# Better solution

def to_encrypt(text, delta):
    """
    98-13=85-97=-12%26=14+97=current locations
    """
    t = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    x = [chr(ord('a') + (ord(i) + delta - ord('a')) % 26) if i in t else i for i in text ]
    
    return ''.join(x)
                

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")


Sun Angle Problem
def sun_angle(time):
    # Extract hours and minutes
    hours,minutes = map(int,time.split(":"))
    sun_angle = 15*hours+minutes/4-90
    if 0 <= sun_angle <= 180:
        return sun_angle
    return "I don't see the sun!"

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")

    
# Say Hi to CheckIO
def say_hi(name: str, age: int) -> str:
    """
        Hi!
    """
    return "Hi. My name is %s and I'm %d years old" % (name,age)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')

Correct Sentence
def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    if not text[0].isupper():
        text = text[0].upper()+ text[1:]
        if not text[-1] == ".":
            text += "."
            return text
        return text
    else:
        if not text[-1] == ".":
            text +="."
            return text
        return text 

# Better Solutions 
# replace the first letter with Upper no matter it is or not
def correct_sentence(text: str) -> str:   
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")




if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    print("Coding complete? Click 'Check' to earn cool rewards!")


# First word
import re
def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    text = re.sub(r"[\.\!\/_,$%^*(+\"\)]+", " ",text)
    text = text.strip()
    first_word = text.split(" ")[0]
    return first_word

Better solutions
def first_word(text: str) -> str:
    """
    re.search 函数返回的结果是 一个Match对象 

    常见的获得对应的值的方法 通过Match对象内的group编号或命名，获得对应的值
    """
    return re.search("([\w']+)", text).group(1)

if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")

def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # check if symbol is in text:
    if text.find(symbol) == -1:
        return None
    else:
        new_text =text.replace(symbol,"",1)
        return (new_text.find(symbol)+1) if new_text.find(symbol) != -1 else None

if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')


#  between_markers
def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # check if both markers in text
    if text.find(begin) != -1 and text.find(end) !=-1:
        return text[(text.find(begin)+len(begin)):text.find(end)] if text.find(end) > text.find(begin) else  ""
    else:
        if text.find(begin) == -1 and text.find(end) != -1:
            return text[:text.find(end)]
        elif text.find(begin) != -1 and text.find(end) == -1:
            return text[(text.find(begin)+len(begin)):]
        return text

# Better solutions
def between_markers(text: str, begin: str, end: str) -> str:
    """
    find the start if there is then find the stop if there is 
    """
    start = text.find(begin) + len(begin) if begin in text else None
    stop = text.find(end) if end in text else None
    return text[start:stop]

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')

# Best_stock
# My straight solution
def best_stock(data):
    # your code here
    stock_value = {value:key for key,value in data.items()}
    value_max = max([a for a in stock_value])      
    return stock_value[value_max]

# Better Solution

def best_stock(data):
"""
For instance, if a class defines a method named __getitem__(), 
and x is an instance of this class, then x[i] is roughly equivalent to type(x).__getitem__(x, i).

"""
    return max(data, key=data.__getitem__)



if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")

#Popular words

# My first to mind solution
def popular_words(text: str, words: list) -> dict:
    # your code here
    text = text.replace("\n"," ")
    text_list = list(map(lambda x: x.lower(),text.split(" ")))
    print(text_list)
    result_dict = {i:0 for i in words}
    for i in words:
        for a in range(0,len(text_list)):
            if text_list[a] == i:
                result_dict[i] += 1
    return result_dict

# Better Solution
def popular_words(text, words):
    """split()分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    text.lower().split().count is not a composition of functions, 
    instead it is the bound method list.count of the list object returned by .split, 
    that is called only once, on the str object returned by .lower, that is called once too. 
    """
    lower_count = text.lower().split().count
    return {word: lower_count(word) for word in words}

if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

#Bigger Price
def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    # your code here
    #返回重新排序的列表。
    sorted_list = sorted(data,key=lambda t:t["price"],reverse=True)
    return sorted_list[:(limit)]


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')