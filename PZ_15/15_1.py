# В матрице найти отрицательные элементы, сформировать из них новый массив.
# Вывести размер полученного массива

from random import randint
m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ")]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print('Исходная матрица:')
for i in matrix:
    print(*i)
count = []
for i in matrix:
    for x in i:
        if x < 0:
            count.append(x)
print(len(count))
