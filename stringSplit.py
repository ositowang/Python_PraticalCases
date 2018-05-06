import re
import os ,stat
import struct
import array
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
# # print(re.split("[:,|\t]+", s))
#
# print(os.listdir('.'))
#
# name_list = [name for name in os.listdir('.') if name.endswith((".py",".txt"))]
#
# print(name_list)
#
# print(oct(os.stat('List_Dict.py').st_mode))
#
# os.chmod("List_Dict.py",os.stat('List_Dict.py').st_mode| stat.S_IXUSER)
#
#
# # Replace the original data with new data format
#
# log = open("mylog.log").read()
#
# re.sub("(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", r"\g<month>/\g<day>/\g<year>", log)


# Read bynary files

f = open('demo.wav', 'rb')
info = f.read(44)

print(f.read(44))
print(struct.unpack('h', info[34:36]))

f.seek(0, 2)
print(f.tell())

n = int((f.tell()-44)/2)

print(n)

buf = array.array("h", [])
f.seek(44)
buf.fromfile(f, n)

print(len(buf))

for x in range(0, n):
    buf[x] = int(buf[x]/8)
    print(buf[x])

f2 = open("demo2.wav", "wb")

f2.write(info)

buf.tofile(f2)

f2.close()








