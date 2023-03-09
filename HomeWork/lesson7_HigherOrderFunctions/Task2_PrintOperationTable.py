# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает
# в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и
# num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание:
# бинарной операцией называется любая операция, у которой ровно два аргумента, как, например,
# у операции умножения.

#  Функция, вычисляющая элемент по номеру строки и столбца
import random

def operation(arr):
    i = int(input('Введите номер строки i: '))
    j = int(input('Введите номер столбца j: '))
    if (i,j) > (n-1,m-1):
        print('Не верно ввели индексы - введите заново')
        return operation(arr) 
    if (i,j) < (0,0):
        print('Не верно ввели индексы - введите заново')
        return operation(arr)                   
    else:
        print(f'Получите элемент массива matrix[{i},{j}]= {arr[i][j]}')




def print_operation_table(operation, num_rows, num_columns):
    matrix = [[random.randrange(0, 20)
               for y in range(1, num_rows + 1)]
              for x in range(1, num_columns + 1)]
    for i in matrix:
        print(*[f'{j:>3}' for j in i])
    # print([print(j, end= ' ') for j in i])
    operation(matrix)


m = int(input('Введите количество строк M =  '))
n = int(input('Введите количество столбцов N = '))
print_operation_table(operation, m, n)
