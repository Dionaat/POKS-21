# . Составить список, в который будут включены только согласные буквы и
# привести их к верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль',
# 'Дели', 'Каир'].

gorod = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
gl = ['а','е', 'ё', 'ю', 'я', 'и', 'о', 'у', 'ы','э','А', 'У', 'Е','Ю', 'Я', 'О','Ё','И', 'Ы' ,'Э']

g = [list(i) for i in list (gorod)]
print(g)

f = []
n = ()

for i in g:
    for j in i:
        for k in gl:
            if j != k:
                n += 1
            if n == len(gl):
                f.append(j)
                break
        n = 0

new_sp = [x.upper()for x in f]
print(new_sp)
