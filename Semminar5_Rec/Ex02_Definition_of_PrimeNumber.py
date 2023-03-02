# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Input: 5
# Output: yes

def chek(number):
    for i in range(2,number):
        if number % i == 0:
            return (f'Число {number} не простое, так как делится на {i} без остатка')
    return (f'Число {number} простое')

number = int(input('Введите число: '))
res = chek(number)
print(res)