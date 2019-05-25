import math

str = input()
for i in str:
    x = ord(i)
    x += 4
    x %= 26
    x += ord(i)
    print(chr(x))