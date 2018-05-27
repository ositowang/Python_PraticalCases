from random import randint,sample
from time import time
from collections import Counter
from collections import namedtuple, OrderedDict
import re
from functools import reduce

# data = [randint(-10, 10) for _ in range(10)]
# # simple filter
# new_data = list(filter(lambda x: x >= 0, data))
# # list parser
# new_data = [x for x in data if x >= 0]
#
#
# dict1 = {x: randint(60,100) for x in range(1, 21)}
# # parse the dict
# dict1 ={k: v for k, v in dict1.items() if v > 90}
#
# print(dict1)
#
# # parse the tuple
# set1 = set(data)
# {x for x in set1 if x%3 ==0}
#
# # Name Tuple index to increase readbility
#
#
# Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
# s = Student("Jim", 16, 'male', "jim1989@gmail.com")
# print(s)
#
# # Count repeating elements in a list
# data1 = [randint(0, 100) for _ in range(30)]
# count_dict = dict.fromkeys(data1, 0)
#
# for x in data1:
#     count_dict[x] += 1
# print(count_dict)
#
# # Easier way with collections.counter
# c2 = Counter(data1)
# print(c2.most_common(3))
#
# # Count the words frequency
# txt = open('TextSplitExample.txt').read()
# txt = re.split("\W+", txt)
# c3 = Counter(txt)
# print(c3.most_common(10))
#
# # Sorted the dict by values
# dict4 = {x: randint(0, 100) for x in "abcdef"}
#
# dict2 = sorted(dict4.items(), key=lambda x: x[1], reverse=True)
# print(dict2)

# Find common keys across dict
s1 = {x: randint(1, 10) for x in sample("abcedfg", randint(3, 6))}
s2 = {x: randint(1, 10) for x in sample("abcedfg", randint(3, 6))}
s3 = {x: randint(1, 10) for x in sample("abcedfg", randint(3, 6))}
s4 = reduce(lambda x, y: x & y, map(dict.keys, [s1, s2, s3]))
print(s4)

# simulate a test

d = OrderedDict()
players = list("ABCEDFGH")
start = time()

for i in range(0,8):
    input("Enter")
    p = players.pop(randint(0, 7-i))
    end = time()
    print(i+1, p, start-end)
    d[p] = (i+1, p, start-end)

print()
print("--"*10)
for x in d:
    print(x, d[x])













