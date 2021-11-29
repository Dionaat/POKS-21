
from math import sqrt, pow

def RectPS():
    a = sqrt(pow((x1 - x1),2) + pow((y1 - y2),2))
    b = sqrt(pow((x1 - x2),2) + pow((y1 - y1),2))
    S = a * b
    P = (a + b) *2

    print("Площадь = ", S)
    print("Периметр = ", P)

x1 = int(input("введите x1: "))
y1 = int(input("введите y1: "))
x2 = int(input("введите x2: "))
y2 = int(input("введите y2: "))

RectPS()

