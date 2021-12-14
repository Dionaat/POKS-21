# дана строка "груши 45 991 63 100 12 морковь 13 47 26 0 16", отражающая продажи продукции по дням в кг.
# Преобразовать информацию из сторки в словари с использованием функции найти мин значения продажи 
# по какому виду продукции результаты вывести на экран

dano = "груши 45 991 63 100 12 морковь 13 47 26 0 16".split(" ")
value_gruh = []
value_morkov = []

for i in dano[1:6]:           # цикл для перебора значений
    value_gruh.append(int(i))
for i in dano[7:]:
    value_morkov.append(int(i))

# создаём словать спомощью срезов
gruh_slovar = {dano[0]: value_gruh}
morkov_slovar = {dano[6]: value_morkov}

# ф-я расчёта выода мин продаж
def min_prod():
    print("Мин продажи груш: ", min(gruh_slovar["груши"]))
    print("Мин продажи моркови: ", min(morkov_slovar["морковь"]))


min_prod()
