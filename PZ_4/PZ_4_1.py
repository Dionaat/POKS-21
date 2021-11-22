# Даны целые числа A и B (A>B). Вывести все целые числа от A до B включительно;
# при этом число A длолжно выводиться 1 раз,число A+1 2 раза и т.д.


# проверка
while True:
    try:
        A = int(input('введите A: '))
        B = int(input('введите B: '))
        if A < B:
            break
        else:
            print('Что-то пошло не так :с попробуй снова')
    except ValueError:
        print('Что-то пошло не так :с попробуй снова')

ans = 0
while A <= B:
    ans += A
    print(str(A) * A)
    A += 1
