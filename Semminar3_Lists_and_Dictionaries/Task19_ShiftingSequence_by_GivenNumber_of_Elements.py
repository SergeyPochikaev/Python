# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность на К элементов в право
# K - положительное число.
# Пример: Input: [1, 2, 3, 4, 5] k = 3
#         Output: [4, 5, 1, 2, 3]
list = [1, 2, 3, 4, 5]
list = list[3:] + list[:len(list)-2]
print(list)

list = [1, 2, 3, 4, 5]
k = 0
for j in range(4):
  for i in range(len(list)-1):
    k = list[i]
    list[i] = list[i+1]
    list[i+1] = k
print(list)