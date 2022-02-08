strok1 = str("3, -4, 12, 14, -10 ")     # создаём строки
strok2 = str("-12, -5, 15, 8, -2 ")

spisok1 = strok1.split(", ")     # делаем из строк списки без запятых и пробела
spisok2 = strok2.split(", ")

file = open("File1.txt", "+w")  # открывааем файл и записываем данные
file.write(strok1)
file.close()

file = open("File2.txt", "+w")   # открывааем файл и записываем данные
file.write(strok2)
file.close()

# обозначаем переменные
proiz = 1
krat3 = []
krat5 = []
sred = 0
dlin = 0

for i in range(len(spisok1)):
    if int(spisok1[i]) % 3 == 0:    # находим числа кратные 3
        rez1 = spisok1[i]
        krat3.append(rez1)
        proiz *= int(spisok1[i])  # находим произведение
rez = min(spisok1)  # находим минимальное число из списка кратных 3

for i in range(len(spisok2)):
    if int(spisok2[i]) % 5 == 0:     # находим числа кратные 5
        rez2 = spisok2[i]
        krat5.append(rez2)
        dlin += 1        # находим количество элементов в списке кратных 5
        sred += int(rez2)
        sred1 = sred // dlin     # находим среднее арифметическое

file = open("newfile.txt", "w+")
# file.write("Содержимое первого файла:")
print("Содержимое первого файла:", open("File1.txt").read(), file=file)
print("Элементы кратные трём(3):", ", ".join(krat3), file=file)
print("Произведение элементов:", str(proiz), file=file)
print("Минимальный элемент:", str(rez), '\n', file=file)

print("Содержимое второго файла:", open("File2.txt").read(), file=file)
print("Элементы кратные пяти(5):", ", ".join(krat5), file=file)
print("Количество элементов:", str(dlin), file=file)
print("Среднее арифмитеческое элементов:", str(sred1), file=file)
file.close()
