# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

import random
list1 = []
for i in range(5):
    i = random.randint(1,5)
    list1.append(i)
print(list1)
count = 0
for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] == list1[j]:
            count += 1
print(count)