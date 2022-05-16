#  В исходном текстовом файле (Dostoevsky.txt) найти все годы деятельности писателя
#  (например, 1821 года, 1837 год, 1843 году и так далее по всему тексту)
#  Посчитать количество полученных элементов.

import re
p = re.compile(r"\d{4}\W+\d{4}\s\w+")
g = re.compile(r"\d{4}\s\w+")
result = []
for i in open('Dostoevsky.txt').read().split('\n'):
    if len(p.findall(i)) > 0:
        result.append(p.findall(i))
    else:
        result.append(g.findall(i))
for i in result:
    if len(i) > 0:
        print(*i)