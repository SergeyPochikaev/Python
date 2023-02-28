# Задача 22: Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

import random
n = int(input('Введите количество кустов: '))
bush = [int(random.randint(0,10)) for i in range(n)]
for i in range(len(bush)):
    print(f'Выросло на кусте {i+1} ягоды в кодичестве: ',bush[i])

module = [bush[i-1]+bush[i]+bush[i+1] for i in range(len(bush)-1)]
module.append(bush[-2]+bush[-1]+bush[0])
print('Итого:')
print(f'Из {n} кустов выросло ягод на каждом кусте: ',bush)
print('Собрано модулем за один ход ягод:',max(module))


