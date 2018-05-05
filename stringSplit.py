import re
import os ,stat
# Split the document with multiple seperator
# s = "ab:cd|efg\t|hi,jkkl"
#
#
# def split_multiple(s, ds):
#     result = [s]
#     for x in ds:
#         t = []
#         list(map(lambda a: t.extend(a.split(x)), result))
#     return t
#
# print(split_multiple(s, ":,|\t"))

# using regular expression
# print(re.split("[:,|\t]+", s))

print(os.listdir('.'))

name_list = [name for name in os.listdir('.') if name.endswith((".py",".txt"))]

print(name_list)

print(oct(os.stat('List_Dict.py').st_mode))

os.chmod("List_Dict.py",os.stat('List_Dict.py').st_mode| stat.S_IXUSER)
