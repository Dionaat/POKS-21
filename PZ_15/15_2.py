# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов.

from random import randint

m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ")]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print('Исходная матрица:')
for i in matrix:
    print(*i)
count = []
for i in range(len(matrix)):
    if i % 2 == 0:
        count.append(sum(matrix[i]) / len(matrix[i]))
print(*count)
