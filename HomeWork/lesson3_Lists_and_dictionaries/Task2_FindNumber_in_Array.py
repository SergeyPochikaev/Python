# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
n = int(input('Введите количество элементов в массиве N = '))
list_1 = [int(random.randint(0,9)) for i in range(n)]
print(*list_1)
x = int(input('Введите любое близкое значение в массиве X = '))
list_2 = [ abs(x - list_1[j]) for j in range(n)]
min = list_2[0]
# list_3 = [k for k in range(len(list_2)) if list_2[k] <= min]
count = 0
for k in range(len(list_2)):
    if list_2[k] <= min:
        min = list_2[k]
        count = k

# print(list_1[list_3[0]])
print(f'Заданное значение {x} близко к значению в массиве {list_1[count]}')