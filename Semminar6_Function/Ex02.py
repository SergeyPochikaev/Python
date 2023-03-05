# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве
# определит количество элементов, у которых два соседних и, при этом,
# оба соседних элемента меньше данного. Сначала вводится число N — 
# количество элементов в массиве. Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел.

def sum (arr):
    count = 0
    for j in arr:
        count += j
    return count

import random
list1 = [random.randint(1,10) for i in range(1,10)]
list2 = [1 for i in range(1, len(list1)-1) if list1[i-1] < list1[i] > list1[i+1]]
print(list1)
print(sum(list2))

# count = 0
# for i in range(1, len(list1)-1):
#     if list1[i-1] < list1[i] > list1[i+1]:
#         count += 1
# print(list1)
# print(count)
    