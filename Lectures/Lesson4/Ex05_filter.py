# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для которых функция вернула True.

data = [x for x in range(10)]
res = list(filter(lambda x: x % 2 == 0, data))
print(res) # [0, 2, 4, 6, 8]

list_1 = '15 65 9 36 175'
res = map(int,list_1.split())
print(list_1)

list_2 = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, list_2))
print(res)