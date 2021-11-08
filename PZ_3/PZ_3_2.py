#

import sys

x1 = input("введите точку где стоит ладья по х: ")
y1 = input("введите точку где стоит по у:  ")
x2 = input("введите точку куда пойдёт ладья:  ")
y2 = input("введите точку куда пойдёт: ")

while True:       #проверка
    try:
        x1 = int(x1)
        y1 = int(y1)
        x2= int(x2)
        y2 = int(y2)
        break
    except ValueError:
        print('Что-то пошло не так :с попробуй снова')
        x1 = input("введите точку где стоит ладья: ")
        y1 = input("введите точку где стоит:  ")
        x2 = input("введите точку куда пойдёт ладья:  ")
        y2 = input("введите точку куда пойдёт: ")

while True:
    if 0 < x1 < 9 and 0 < x2 < 9 and 0 < y1 < 9 and 0 < y2 < 9:
        pass
    else:
        print("ошибка, не выходи за доску")
        sys.exit()
    break

if (x1 == x2) and (y1 == y2):
    print("стоит на месте")
elif (x1 == x2) and (y1 > y2):
    print("ладья идёт вниз")
elif (x1 == x2) and (y1 < y2):
    print("ладья идёт вверх")
elif (x1 < x2) and (y1 == y2):
    print("идёт вправо")
elif (x1 > x2) and (y1 == y2):
    print("ладья идёт влево")
else:
    print("ладья не ходит по диагонали")