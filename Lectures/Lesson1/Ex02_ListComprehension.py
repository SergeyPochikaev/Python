# Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1)  # [1, 2, 3,..., 100]
print()
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
print(list_1)
