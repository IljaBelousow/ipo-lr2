from math import asin
from math import sqrt
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z (от -1 до 1) = "))
b = sqrt(10 * (x ** (1/3) + (x ** (y + 2)))) * ((asin(z) ** 2) - abs(x - y))
print(b)
