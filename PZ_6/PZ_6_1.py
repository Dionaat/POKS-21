# дан список ненулевых чисел размера Н. проверить, образуют ли его элементы геометрическую прогрессию.
# Если дf, то вывести знаменатель прогрессии, если нето вывести 0

a = []
n = int(input('Введите кол-во элементов: '))

inp = int
while n:
    while True:
        inp = int(input('Введите число: '))
        if inp == 0:
            print('!!Число не должно быть нулём!!')
        else:
            break
    a.append(inp)
    n -= 1

t = bool
p = 0
d = float
for i in range(1, len(a), - 1):
    if a[i] / a[i - 1] == a[i + 1] / a[i]:
        p += 1

t = p == len(a) - 2
if t:
    print('Является геометрической прогрессией ')
    d = a[1] / a[0]
    print(d)
else:
    print('Не является геометрической прогрессией')
