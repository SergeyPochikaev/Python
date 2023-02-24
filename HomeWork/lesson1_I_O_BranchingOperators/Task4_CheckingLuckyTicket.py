# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

# Ввод т вывод шаколадки
print('Введите размер шаколадной плитки mxn:')
m = int(input('Введите m = '))
n = int(input('Введите n = '))
print('Получите вашу целую шаколадку:')
for i in range(m):
    lin = ""
    for j in range(n):
        lin += "# "
    print(lin)
print()

# Ввод количество долек k
print('Насколько долек k вы хотите поделить эту шаколадку,')
print('если делите по всей длине или ширене!')
k = int(input('Введите количество долек k = '))

# Условие деление шаколадки на равное количество долек k
if (k >= m or k >= n) and k < m*n:
    if k % m != 0 or k % n != 0:
        print('Не возможно поделить шаколадку, задайте другое количество долек')
    d = int(k / m)
    if k % m == 0:
        print(f'Получите дольки {k} в одной форме:')
        for i in range(m):
            string = ''
            for j in range(d):
                string += '# '
            print(string)
    print()
    if k % n == 0:
        print(f'Получите дольки {k} в другой форме:')
        for i in range(d):
            string = ''
            for j in range(int(n)):
                string += '# '
            print(string)
else:
    print('Не возможно поделить шаколадку, задайте другое количество долек')