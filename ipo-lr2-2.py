from math import floor
apple = int(input('apple = '))
school = int(input('shool = '))
a = apple
s = school
b = a % s
c = floor(a / s)
print(b)
print(c)