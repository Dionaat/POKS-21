# Даны значения роста 20 юношей. Определить сколько юношей будут направлены в баскетбольную команду (рост от 190)
# и сколько в футбольную (остальные)
from random import *

rost = [randrange(160, 200) for i in range(20)]
print(rost)

rostak = [i for i in rost if i >= 190]
print("сколько идёт на баскетбол: ", len(rostak))

rostik = [i for i in rost if i < 190]
print("остальные: ", len(rostik))
