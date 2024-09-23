from math import sqrt
from math import asin
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
b = sqrt(10 * (x ** (1/3) + x ** (y + 2)))*((asin(z) ** 2) - abs(x - y))
print(b)